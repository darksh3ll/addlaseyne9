# admin.py
from django.contrib import admin
from .models import TeamMember,GalleryPhoto,LiveStream

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')
    search_fields = ('first_name', 'last_name', 'role')


admin.site.register(GalleryPhoto)

@admin.register(LiveStream)
class LiveStreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'start_time', 'youtube_link')
    search_fields = ('title', 'subtitle', 'youtube_link')
    list_filter = ('start_time',)
