from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify  # new

class Testimonial(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title", blank=False)
    slug = models.SlugField(null=False, unique=True)  # new
    author_name = models.CharField(max_length=100, verbose_name="Author's Name", blank=False)
    publication_date = models.DateField(verbose_name="Publication Date", blank=False)
    text = models.TextField(verbose_name="Testimonial Text", blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("testimonial_detail", kwargs={"slug": self.slug})
    

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
