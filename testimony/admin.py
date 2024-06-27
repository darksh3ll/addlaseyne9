from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'publication_date', 'text')
    search_fields = ('title', 'author_name', 'text')
    list_filter = ('publication_date',)

