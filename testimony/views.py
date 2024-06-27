from django.shortcuts import render
from .models import Testimonial
def testimony_view(request):
    testimonials = Testimonial.objects.all()
    for testimonial in testimonials:
        print(testimonial)

    context = {
        'testimonials': testimonials,
    }

    
    return render(request, 'testimony.html', context)