from django.db import models

class Services(models.Model):
    help = "ALL SERVICES"
    title = models.CharField("Titles", max_length=200)   
    des = models.TextField("Description")
    style_name = models.CharField("Style Name", max_length=200, null=True, blank=True)  
    main_image = models.ImageField("Image in detail page (600X450)", upload_to='images/%y%m%d', blank=True, null=True)      
  
    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "ALL SERVICES"
        verbose_name = "ALL SERVICES"

class Partners(models.Model):
    help = "ALL PARTNERS"
    title = models.CharField("Titles", max_length=200)   
    image = models.ImageField(upload_to='images/%y%m%d', blank=True)

    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "ALL PARTNERS"
        verbose_name = "ALL PARTNERS"