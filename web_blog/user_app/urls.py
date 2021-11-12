from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('', views.MainScreen.as_view(), name='index'),
    path(r'index', views.MainScreen.as_view(), name='index_filters'),
    path(r'blog', views.MainScreen.as_view(), name='index_pages'),
    path('ver/<str:post_title>', views.SeePost.as_view(), name='see_post'),
    path('agregarPublicacion', views.CreatePost.as_view(), name='create_post'),
    path('logout', LogoutView.as_view(), name='logout'),
]
