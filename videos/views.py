from django.shortcuts import render

# Create your views here.
def videos_list(request):
    return render(request, 'videos_list.html')