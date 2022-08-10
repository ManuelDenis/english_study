
import datetime

from django.contrib.auth.models import User, Group
from django.views.generic import ListView, TemplateView
from agency.models import RomEng, RomEngExp, EngRomVerbs, WayToSay
from payments.models import UserProfile


class HomeView(TemplateView):
    template_name = 'agency/home.html'


class ArticleView(ListView):
    model = RomEng
    template_name = 'agency/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exp_list'] = RomEng.objects.all().order_by("?")[:50]
        return context


class WayToSayView(ListView):
    model = WayToSay
    template_name = 'agency/waytosay.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exp_list'] = WayToSay.objects.all().order_by("?")[:50]
        return context


class ArticleEasyView(ListView):
    model = RomEngExp
    template_name = 'agency/article_easy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exp_list_2'] = RomEngExp.objects.all().order_by("?")[:50]
        return context


class EngRomVerbsView(ListView):
    model = EngRomVerbs
    template_name = 'agency/verbs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = EngRomVerbs.objects.all().order_by("?")[:50]
        context['exp_list_2'] = a
        return context
