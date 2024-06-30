from django.shortcuts import render
from testimony.models import Testimonial
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    title = 'lorem10'
    testimonial_list = Testimonial.objects.all()

    team_members = [
        {"name": "reinhard boonke", "title": "Evangeliste",
            "image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQsZEL1wDx5LhaUo9TEHAL2o-6YDMqvK5UEyP5HkzGHccm4JyCE"},
        {"name": "Yahya R. Makarim", "title": "President & CEO",
            "image": "https://images.pexels.com/photos/2897883/pexels-photo-2897883.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"},
        {"name": "Ahmad Sultani", "title": "Web designer",
            "image": "https://images.pexels.com/photos/3778680/pexels-photo-3778680.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"},
        {"name": "Mehdi Mohammadi", "title": "Web developer",
            "image": "https://images.pexels.com/photos/1587014/pexels-photo-1587014.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"},
        {"name": "Yahya R. Makarim", "title": "President & CEO",
            "image": "https://images.pexels.com/photos/2897883/pexels-photo-2897883.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"},
        {"name": "Ahmad Sultani", "title": "chef groupe coral",
            "image": "https://images.pexels.com/photos/3778680/pexels-photo-3778680.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"},
    ]
    address = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d480.5462847513066!2d5.88154952529991!3d43.09426159991749!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12c9035c5ebb7e0d%3A0xdba473d9c39c9e3a!2sRue%20Alexandre%20Ghibaudo!5e0!3m2!1sen!2sid!4v1718898242201!5m2!1sen!2sid'
    return render(request, 'index.html', {'team_members': team_members, 'address': address, 'title': title, 'testimonials': testimonial_list})


def donate(request):
    return render(request, 'donate.html')
