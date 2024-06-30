from django.shortcuts import render
from .models import Testimonial


def testimony_detail_view(request):
    return render(request, 'testimonial_detail.html')