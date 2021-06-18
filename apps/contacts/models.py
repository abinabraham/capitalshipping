from django.db import models

class ContactedDetails(models.Model):
    help = "Contacted Details"
    name = models.CharField("Name", max_length=200)  
    email = models.CharField("Email", max_length=200)  
    mobile = models.CharField("Mobile", max_length=200, null=True, blank=True)  
    des = models.TextField("Query")


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Contacted Details"
        verbose_name = "Contacted ContactedDetailsDetails"