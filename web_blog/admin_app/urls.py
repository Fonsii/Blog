from django.urls import path
from . import views

urlpatterns = [
    path('administracion/categorias', views.AdministrationView.as_view(), name='administration_categories'),
    path(r'administracion/categorias/<int:category>',
         views.AdministrationView.as_view(), name='administration_categories'),
]
