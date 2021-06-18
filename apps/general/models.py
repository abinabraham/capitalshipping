from django.db import models

class HeaderConfig(models.Model):
    help = "HeaderConfig"
    mail = models.CharField("Company Email ID", max_length=200)  

    logo = models.ImageField("Company LOGO", upload_to='gallery/images/%y%m%d', blank=True)

    fb_url = models.CharField("FB URL", max_length=250, null=True, blank=True)
    tw_url = models.CharField("TWITTER URL", max_length=250, null=True, blank=True)
    rss_url = models.CharField("RSS FEED", max_length=250, null=True, blank=True)
    gp_url = models.CharField("Google PLUS URL", max_length=250, null=True, blank=True)





    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mail

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Header Configurations"
        verbose_name = "Header Configurations"



class FooterOurService(models.Model):
    help = "Footer Our Service"
    title = models.CharField("Title", max_length=200)  
    url = models.CharField("url eg: '/services/'", max_length=250, null=True, blank=True)





    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Footer Our Service"
        verbose_name = "Footer Our Service"

class Address(models.Model):
    help = "Address"
    line1 = models.CharField("line1", max_length=200)  
    line2 = models.CharField("line2", max_length=200)
    line3 = models.CharField("line3", max_length=200)
    line4 = models.CharField("line4", max_length=200)

    phone = models.CharField("Phone", max_length=200)
    email = models.CharField("Email", max_length=200)

    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.line1

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Address"
        verbose_name = "Address"