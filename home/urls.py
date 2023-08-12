from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('', views.hello, name='hello')
    path('', TemplateView.as_view(template_name='index.html')),
]