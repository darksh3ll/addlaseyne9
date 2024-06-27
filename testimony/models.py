from django.db import models

# Create your models here.
from django.db import models

class Testimonial(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    author_name = models.CharField(max_length=100, verbose_name="Author's Name")
    publication_date = models.DateField(verbose_name="Publication Date")
    text = models.TextField(verbose_name="Testimonial Text")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
