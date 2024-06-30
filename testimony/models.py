from django.db import models

class Testimonial(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title", blank=False)
    author_name = models.CharField(max_length=100, verbose_name="Author's Name", blank=False)
    publication_date = models.DateField(verbose_name="Publication Date", blank=False)
    text = models.TextField(verbose_name="Testimonial Text", blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
