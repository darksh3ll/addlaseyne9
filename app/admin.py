# admin.py
from django.contrib import admin
from .models import TeamMember,GalleryPhoto,CarouselItem,ChurchInfo

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')
    search_fields = ('first_name', 'last_name', 'role')

@admin.register(ChurchInfo)
class ChurchInfoAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
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
            'fields': ('name', 'street_number', 'street_name', 'city', 'postal_code', 'country', 'phone', 'mobile_phone', 'email', 'rib_number')
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