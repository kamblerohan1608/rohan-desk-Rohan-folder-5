from django.db import models

# Create your models here.

class Amenities(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    
class Hotels(models.Model):

    hotel_name = models.CharField(max_length=200)
    hotel_desc = models.TextField()
    hotel_image = models.ImageField(upload_to = 'hotel_pics/')
    price = models.FloatField()
    amenities = models.ManyToManyField(Amenities)


    def __str__(self):
        return self.hotel_name