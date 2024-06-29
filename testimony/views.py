from django.shortcuts import render
from .models import Testimonial
def testimony_view(request):

    context = {
        'title':"laurent"
    }

    
    return render(request, 'testimony.html',context)