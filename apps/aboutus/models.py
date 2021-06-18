from django.db import models

class AboutIntro(models.Model):
    help = "AboutIntro"
    title = models.CharField("Titles", max_length=200)
    des = models.TextField("Description")   
    image = models.ImageField("Image (800X400)", upload_to='about/images/%y%m%d', blank=True)

    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "About Intro"
        verbose_name = "About Intro"

class DirectorsBoard(models.Model):
    help = "Directors Board"
    title = models.CharField("Titles", max_length=200)
    role = models.CharField("Role", max_length=200)
    des = models.TextField("Description")   
    image = models.ImageField("Profile Image (255X255)", upload_to='about/images/%y%m%d', blank=True)

    fb_url = models.CharField("FB URL", max_length=250, null=True, blank=True)
    tw_url = models.CharField("TWITTER URL", max_length=250, null=True, blank=True)
    gp_url = models.CharField("Google PLUS URL", max_length=250, null=True, blank=True)
    in_url = models.CharField("INSTAGRAM URL", max_length=250, null=True, blank=True)
    pin_url = models.CharField("PINTEREST URL", max_length=250, null=True, blank=True)

    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Directors Board"
        verbose_name = "Directors Board"


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