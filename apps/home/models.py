from django.db import models


class WhyChooseUs(models.Model):
    help = "WHY_CHOOSE_US"
    title = models.CharField("Titles", max_length=200)   
    des = models.TextField("Description")   
    style_name = models.CharField("Style Name", max_length=200, null=True, blank=True)    

  
    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "WHY_CHOOSE_US"
        verbose_name = "WHY_CHOOSE_US"

class Whoweare(models.Model):
    help = "WHO_WE_ARE"
    title = models.CharField("Titles", max_length=200)   
    des = models.TextField("Description")
    style_name = models.CharField("Style Name", max_length=200, null=True, blank=True)        
  
    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "WHO_WE_ARE"
        verbose_name = "WHO_WE_ARE"