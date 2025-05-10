from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import (
    TeamMember, GalleryPhoto, CarouselItem, ChurchInfo,
    LiveStream, LatestYouTubeVideo, ChurchSchedule,
    GlobalSiteImages, LatestTestimonyVideo, Testimony
)


def index(request):
    title = 'lorem10'
    team_members = TeamMember.objects.all()
    photo_gallery = GalleryPhoto.objects.all()
    carousel_items = CarouselItem.objects.all()
    stream = LiveStream.objects.last()
    church_info = ChurchInfo.objects.first()
    latest_video = LatestYouTubeVideo.objects.last()
    latest_testimony = LatestTestimonyVideo.objects.last()
    schedule = ChurchSchedule.objects.all()
    global_images = GlobalSiteImages.objects.first()
    testimonies = Testimony.objects.all().order_by("-published_date")[:6] 

    context = {
        'team_members': team_members,
        'title': title,
        'photo_gallery': photo_gallery,
        'carousel_items': carousel_items,
        'church_info': church_info,
        'stream': stream,
        'latest_video': latest_video,
        'latest_testimony': latest_testimony,
        'schedule': schedule,
        'global_images': global_images,
        'testimonies': testimonies,
    }

    return render(request, 'index.html', context)


def donate(request):
    church_info = ChurchInfo.objects.first()
    rib_number = church_info.rib_number if church_info else "Numéro de RIB non disponible"
    return render(request, 'donate.html', {'rib_number': rib_number})


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


# ✅ Témoignages : recherche sans pagination
def testimonies_view(request):
    query = request.GET.get("q", "").strip()
    testimonies = Testimony.objects.all().order_by("-published_date")

    if query:
        testimonies = testimonies.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__name__icontains=query) |
            Q(author__icontains=query)
        )

    return render(request, "testimonies.html", {
        "testimonies": testimonies,
        "query": query
    })

def testimony_detail(request, slug):
    testimony = get_object_or_404(Testimony, slug=slug)
    return render(request, 'testimony_detail.html', {'testimony': testimony})