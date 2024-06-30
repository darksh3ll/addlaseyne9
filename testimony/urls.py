from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimony_detail_view, name='testimonial_detail'),
]