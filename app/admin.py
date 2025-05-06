# admin.py
from django.contrib import admin
from .models import TeamMember,GalleryPhoto,CarouselItem,ChurchInfo,LiveStream,LatestYouTubeVideo,ChurchSchedule,GlobalSiteImages
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')
    search_fields = ('first_name', 'last_name', 'role')

@admin.register(ChurchInfo)
class ChurchInfoAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'logo',
        'street_number', 
        'street_name', 
        'city', 
        'postal_code', 
        'country', 
        'phone', 
        'mobile_phone', 
        'email', 
        'rib_number', 
        'facebook', 
        'instagram', 
        'twitter', 
        'youtube', 
        'google_maps_url'
    )

    fieldsets = (
        ('Informations Générales', {
            'fields': ('name','logo', 'street_number', 'street_name', 'city', 'postal_code', 'country', 'phone', 'mobile_phone', 'email', 'rib_number')
        }),
        ('Réseaux Sociaux', {
            'fields': ('facebook', 'instagram', 'twitter', 'youtube')
        }),
        ('Autres', {
            'fields': ('google_maps_url',)
        }),
    )
admin.site.register(GalleryPhoto)

admin.site.register(CarouselItem)

admin.site.register(LiveStream)

@admin.register(LatestYouTubeVideo)
class LatestYouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ("video_embed_url",)
    

@admin.register(ChurchSchedule)
class ChurchScheduleAdmin(admin.ModelAdmin):
    list_display = ("image", "uploaded_at")




@admin.register(GlobalSiteImages)
class GlobalSiteImagesAdmin(admin.ModelAdmin):
    list_display = ('__str__',)