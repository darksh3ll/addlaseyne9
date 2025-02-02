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
    

class ChurchInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom de l'église", blank=False)
    street_number = models.CharField(max_length=10, verbose_name="Numéro de rue", blank=False)
    street_name = models.CharField(max_length=255, verbose_name="Nom de la rue", blank=False)
    city = models.CharField(max_length=255, verbose_name="Ville", blank=False)
    postal_code = models.CharField(max_length=10, verbose_name="Code postal", blank=False)
    country = models.CharField(max_length=255, verbose_name="Pays", blank=False)
    phone = models.CharField(max_length=20, verbose_name="Téléphone", blank=False)
    mobile_phone = models.CharField(max_length=20, verbose_name="Téléphone portable", blank=False)
    rib_number = models.CharField(max_length=34, verbose_name="Numéro RIB", blank=False)
    email = models.EmailField(verbose_name="Email", blank=False)  # Nouveau champ pour email
    facebook = models.URLField(verbose_name="Facebook", blank=True)
    instagram = models.URLField(verbose_name="Instagram", blank=True)
    twitter = models.URLField(verbose_name="Twitter", blank=True)
    youtube = models.URLField(verbose_name="YouTube", blank=True)  # Nouveau champ pour YouTube
    google_maps_url = models.URLField(verbose_name="Google Maps URL", blank=True)  # Nouveau champ pour Google Maps

    class Meta:
        verbose_name = "Information de l'église"
        verbose_name_plural = "Informations de l'église"

    def __str__(self):
        return self.name



class LiveStream(models.Model):
    iframe_code = models.TextField(verbose_name="Code Iframe")

    def __str__(self):
        return "Live Stream"


class LatestYouTubeVideo(models.Model):
    video_embed_url = models.URLField(
        "URL intégrée de la dernière vidéo",
        help_text="Collez ici l'URL du format iframe YouTube (ex: https://www.youtube.com/embed/VIDEO_ID)."
    )

    def __str__(self):
        return f"Dernière vidéo : {self.video_embed_url}"

    
class ChurchSchedule(models.Model):
    image = models.ImageField(
        "Image des horaires",
        upload_to="church_schedules/",
        help_text="Téléchargez une image contenant les horaires de l'église."
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Horaires de l'église ({self.uploaded_at.strftime('%d/%m/%Y')})"