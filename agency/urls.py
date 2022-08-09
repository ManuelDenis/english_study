from django.urls import path
from agency.views import ArticleView, ArticleEasyView, EngRomVerbsView, HomeView, WayToSayView

urlpatterns = [
    path('', ArticleView.as_view(), name='articles'),
    path('article_easy/', ArticleEasyView.as_view(), name='article_easy'),
    path('waytosay/', WayToSayView.as_view(), name='waytosay'),
    path('verbs/', EngRomVerbsView.as_view(), name='verbs'),
    path('home/', HomeView.as_view(), name='home'),
]