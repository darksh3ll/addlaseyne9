from django.shortcuts import render
from testimony.models import Testimonial
from .models import TeamMember
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    title = 'lorem10'
    testimonials = Testimonial.objects.filter(is_active=True)
    team_members = TeamMember.objects.all()
    
    # team_members = [
    #     {
    #         "name": "Cyril Pouget",
    #         "title": "Pasteur principal",
    #         "image": "https://images.pexels.com/photos/842980/pexels-photo-842980.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    #     },
    #     {
    #         "name": "Yahya R. Makarim",
    #         "title": "President & CEO",
    #         "image": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww1.cbn.com%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Foriginal%2Fpublic%2Fmedia%2Fstandard%2Fimages%2Fsue574_reinhard_bonnke_si.jpg%3Fitok%3DcfgJMDfn&f=1&nofb=1&ipt=0426b95d49c3f0dab862326b58bffc50213393690e8a48fb0bf3b6e04afe5c9f&ipo=images"
    #     },
    #     {
    #         "name": "Laurence Sultani",
    #         "title": "Responsable chorale",
    #         "image": "https://images.pexels.com/photos/1036623/pexels-photo-1036623.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    #     },
    # ]
    
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
    }
    
    return render(request, 'index.html', context)

def donate(request):
    return render(request, 'donate.html')
