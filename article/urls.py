from django.urls import path,re_path
from article import views as article_views

urlpatterns = [
    path('',article_views.index,name='index'),
    path('all_article/',article_views.all_article,name='all_article'),
    path('about/',article_views.about,name='about'),
    path('article/<int:id>',article_views.article,name='article')
]