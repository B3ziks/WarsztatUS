from django.db import models
from django.db.models import Model


# Create your models here.
class Pricing(models.Model):
    UPLOAD_TO="pricing/"
    service_name = models.CharField(max_length=128,default="",verbose_name="nazwa_uslugi");
    service_number = models.DecimalField(max_digits=20, decimal_places=0,verbose_name="numer_uslugi");
    price = models.DecimalField(max_digits=20, decimal_places=0, verbose_name="cena");
    vehicle = models.CharField(max_length=128, default="", verbose_name="rodzaj pojazdu");
    description= models.TextField(max_length=1024,default="",null=True,blank=True, verbose_name="opis")
    image=models.ImageField(upload_to=UPLOAD_TO,null=True,blank=True, verbose_name="zdjecie")
    
    class Meta:
        ordering=["service_number"]

