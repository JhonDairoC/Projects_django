from django.db import models

# Create your models here.

class Produc(models.Model):
    id = models.AutoField(primary_key=True)
    clasific = models.CharField(max_length=30, blank=False, null=False)
    name = models.CharField(max_length=30, blank=False, null=False)  
    price = models.IntegerField()
    image = models.CharField(max_length=150, blank=False, null=False)
    supplier = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.__all__