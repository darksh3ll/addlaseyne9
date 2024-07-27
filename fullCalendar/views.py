
from django.shortcuts import render
from .models import Event

def calendar_view(request):
    events = Event.objects.all()
    events_list = []
    for event in events:
        events_list.append({
            'title': event.title,
            'description': event.description,
            'start': event.start_time.isoformat(),
            'end': event.end_time.isoformat(),
        })
    context = {
        'events': events_list
    }
    return render(request, 'calendar_view.html', context)