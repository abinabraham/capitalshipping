from django.db import models

class Gallery(models.Model):
    help = "Gallery"
    title = models.CharField("Titles", max_length=200)  
    image = models.ImageField("Profile Image (700X448)", upload_to='gallery/images/%y%m%d', blank=True)



    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Gallery"
        verbose_name = "Gallery"