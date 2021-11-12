from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('', views.MainScreen.as_view(), name='index'),
    path(r'index', views.MainScreen.as_view(), name='index_filters'),
    path(r'blog', views.MainScreen.as_view(), name='index_pages'),
    path('ver/<int:post>', views.ViewPost.as_view(), name='view_post'),
    path('agregarPublicacion', views.CreatePost.as_view(), name='create_post'),
    path('logout', LogoutView.as_view(), name='logout'),
]
