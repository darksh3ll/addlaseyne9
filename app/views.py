from django.shortcuts import render
from testimony.models import Testimonial
from .models import TeamMember,GalleryPhoto,CarouselItem,ChurchInfo,LiveStream,LatestYouTubeVideo,ChurchSchedule
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    title = 'lorem10'
    testimonials = Testimonial.objects.filter(is_active=True)
    team_members = TeamMember.objects.all()
    photo_gallery = GalleryPhoto.objects.all()
    carousel_items = CarouselItem.objects.all()
    stream = LiveStream.objects.last()
    # Récupération des informations de l'église
    church_info = ChurchInfo.objects.first()
    latest_video = LatestYouTubeVideo.objects.last()
    schedule = ChurchSchedule.objects.all()
    
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
        'photo_gallery':photo_gallery,
        'carousel_items':carousel_items,
        'church_info': church_info,
        'stream':stream,
        'latest_video':latest_video,
        "schedule": schedule
        
    }

    
    return render(request, 'index.html', context)

def donate(request):
    church_info = ChurchInfo.objects.first()  # Supposons qu'il n'y a qu'une seule entrée pour l'église
    rib_number = church_info.rib_number if church_info else "Numéro de RIB non disponible"
    return render(request, 'donate.html', {'rib_number': rib_number})


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


