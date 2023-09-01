from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', TemplateView.as_view(template_name='react_app.html')),
    path('uploads/', views.upload_file, name='upload'),
    path('reactApp/', TemplateView.as_view(template_name='react_app.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)