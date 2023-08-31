from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.hello, name='hello'),
    # TODO. react로 작성한 페이지도 로드 되게끔
    # path('', TemplateView.as_view(template_name='index.html')),

    path('uploads/', views.upload_file, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)