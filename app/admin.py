# admin.py
from django.contrib import admin
from .models import TeamMember,GalleryPhoto,CarouselItem

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')
    search_fields = ('first_name', 'last_name', 'role')


admin.site.register(GalleryPhoto)

admin.site.register(CarouselItem)