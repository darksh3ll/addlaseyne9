from django.urls import path
from . import views

urlpatterns = [
    path("testimonial_detail/<slug:slug>", views.testimony_detail_view, name='testimonial_detail'),
]