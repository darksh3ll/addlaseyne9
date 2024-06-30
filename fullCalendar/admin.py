
from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time')
    fields = ('title', 'start_time', 'end_time')

admin.site.register(Event, EventAdmin)
# admin.site.register(Event)