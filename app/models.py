from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name", blank=False)
    last_name = models.CharField(max_length=100, verbose_name="Last Name", blank=False)
    role = models.CharField(max_length=100, verbose_name="Role", blank=False)
    image = models.ImageField(upload_to='team_images/', verbose_name="Image")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"
    
    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"


class GalleryPhoto(models.Model):
    image = models.ImageField(upload_to='gallery_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo uploaded on {self.uploaded_at}"
    

class CarouselItem(models.Model):
    img_src = models.ImageField(upload_to='carrousel/')
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description',max_length=139)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "images_carrousels"
        verbose_name_plural = "images_carrousels"

    def __str__(self):
        return self.title