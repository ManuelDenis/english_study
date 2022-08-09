import datetime
import stripe
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from payments.models import Price, Product, UserProfile

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.BASE_URL + '/payments/success/',
            cancel_url=settings.BASE_URL + '/payments/cancel/',
        )
        return redirect(checkout_session.url)


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "payments/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if UserProfile.objects.filter(user=self.request.user).exists():
            user_prof = UserProfile.objects.get(user=self.request.user)
            user_prof.end_data_pay = datetime.date.today() + datetime.timedelta(365)
            user_prof.save()
        else:
            new_user = UserProfile(user=self.request.user)
            new_user.save()

        user_group = Group.objects.get(name='active')
        self.request.user.groups.add(user_group)
        context['user_cli'] = User.objects.get(email=self.request.user.email)
        return context


class CancelView(TemplateView):
    template_name = "payments/cancel.html"


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "payments/home.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Basic Plan")
        prices = Price.objects.filter(product=product)
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context


@require_POST
@csrf_exempt
def stripe_webhook_paid_endpoint(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    # Try to validate and create a local instance of the event
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_SIGNING_SECRET)
    except ValueError as e:
        # Invalid payload
        return SuspiciousOperation(e)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return SuspiciousOperation(e)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        checkout_session = event['data']['object']
        # Make sure is already paid and not delayed
        if checkout_session.payment_status == "paid":
            client = User.objects.get(user=request.user)
            return redirect('success', {client: client})

    # Passed signature verification
    return HttpResponse(status=200)


def _handle_successful_payment(checkout_session):
    return render(request, 'payments/success.html')
