from django.shortcuts import render
from .models import TeamMember,GalleryPhoto,CarouselItem,ChurchInfo,LiveStream,LatestYouTubeVideo,ChurchSchedule,GlobalSiteImages



def index(request):
    title = 'lorem10'
    team_members = TeamMember.objects.all()
    photo_gallery = GalleryPhoto.objects.all()
    carousel_items = CarouselItem.objects.all()
    stream = LiveStream.objects.last()
    # Récupération des informations de l'église
    church_info = ChurchInfo.objects.first()
    latest_video = LatestYouTubeVideo.objects.last()
    schedule = ChurchSchedule.objects.all()
    global_images = GlobalSiteImages.objects.first()
    
    context = {
        'team_members': team_members,
        'title': title,
        'photo_gallery':photo_gallery,
        'carousel_items':carousel_items,
        'church_info': church_info,
        'stream':stream,
        'latest_video':latest_video,
        "schedule": schedule,
        'global_images': global_images,
        
    }

    
    return render(request, 'index.html', context)

def donate(request):
    church_info = ChurchInfo.objects.first()  # Supposons qu'il n'y a qu'une seule entrée pour l'église
    rib_number = church_info.rib_number if church_info else "Numéro de RIB non disponible"
    return render(request, 'donate.html', {'rib_number': rib_number})


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


