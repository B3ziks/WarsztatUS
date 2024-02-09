from django.db import models
from django.db.models import Model


# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="Nazwa");
    description= models.TextField(max_length=1024,default="",null=True,blank=True, verbose_name="Opis");
    class Meta:
        ordering=["name"]
    def __str__(self):
        return f"{self.name}"
# Create your models here.
class Employee(models.Model):
    UPLOAD_TO="employee/"
    first_name = models.CharField(max_length=128,default="",verbose_name="Imię");
    last_name = models.CharField(max_length=256,default="",verbose_name="Nazwisko");
    birth_date = models.DateField(null=True,verbose_name="Data urodzenia");
    description= models.TextField(max_length=1024,default="",null=True,blank=True, verbose_name="Opis");
    image=models.ImageField(upload_to=UPLOAD_TO,null=True,blank=True, verbose_name="Zdjęcie")
    position=models.ForeignKey(Position, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Stanowisko")
    HIRED="h"
    DISMISSED="d"
    TERMINATED="t"
    STATUSES=[(HIRED, "zatrudniony"),
              (DISMISSED, "zwolniony"),
              (TERMINATED, "wypowiedzenie"),]
    status=models.CharField(max_length=1,choices=STATUSES,default=HIRED)
    
    
    def status_name(self):
        for status in self.STATUSES:
            if status[0]==self.status:
                return status[1]
        return ""
    
    class Meta:
        ordering=["last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.birth_date.year}"