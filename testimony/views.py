from django.shortcuts import render
from .models import Testimonial
from django.shortcuts import render, get_object_or_404

def testimonial_detail(request, slug):
    testimonial = get_object_or_404(Testimonial, slug=slug)
    return render(request, 'testimonial_detail.html', {'testimonial': testimonial})