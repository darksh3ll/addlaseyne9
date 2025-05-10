from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('donate/', views.donate, name='donate'),
    path('temoignages/', views.testimonies_view, name='testimonies'),
    path('temoignage/<slug:slug>/', views.testimony_detail, name='testimony_detail'),
]
