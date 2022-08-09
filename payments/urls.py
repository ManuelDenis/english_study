from django.urls import path
from payments.views import CancelView, SuccessView, CreateCheckoutSessionView, HomePageView, stripe_webhook_paid_endpoint

urlpatterns = [
    path('', HomePageView.as_view(), name='homes'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('stripe-webhook-paid/', stripe_webhook_paid_endpoint),
]
