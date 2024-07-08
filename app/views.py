from django.shortcuts import render
from testimony.models import Testimonial
from .models import TeamMember,GalleryPhoto
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    title = 'lorem10'
    testimonials = Testimonial.objects.filter(is_active=True)
    team_members = TeamMember.objects.all()
    photo_gallery = GalleryPhoto.objects.all()
    address = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d480.5462847513066!2d5.88154952529991!3d43.09426159991749!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12c9035c5ebb7e0d%3A0xdba473d9c39c9e3a!2sRue%20Alexandre%20Ghibaudo!5e0!3m2!1sen!2sid!4v1718898242201!5m2!1sen!2sid'
   
    # Pagination
    paginator = Paginator(testimonials, 8)  # Affiche 3 témoignages par page
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'team_members': team_members,
        'address': address,
        'title': title,
        'page_obj': page_obj,
        'photo_gallery':photo_gallery
    }
    
    return render(request, 'index.html', context)

def donate(request):
    return render(request, 'donate.html')
