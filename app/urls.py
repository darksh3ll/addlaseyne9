from django.urls import path,include

from config import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('donate/', views.donate, name='donate'),

  
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)