from django.db import models

class Mobile(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    #mobile_logo = models.FileField()

    def __str__(self):
        return self.name

class Toys(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    #toys_logo = models.FileField()


    def __str__(self):
        return self.name

