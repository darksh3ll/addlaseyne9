from django.urls import path
from . import views

urlpatterns = [
    path("testimonial_detail/<slug:slug>", views.testimonial_detail, name='testimonial_detail'),
]