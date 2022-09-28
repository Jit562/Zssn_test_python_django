from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female"),
    ("other", "other"),
    
)

class Baseclass(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract=True


class Survivor(Baseclass):
    name = models.CharField(max_length=120, blank=True, null=True)
    age = models.CharField(max_length= 20, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=" ")

    class Meta:
        ordering = ['name']


    def __str__(self):

        return self.name  

class Location(Baseclass):
    survivor = models.ForeignKey(Survivor, related_name="locations",  on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=6, decimal_places = 2)
    long = models.DecimalField(max_digits=6, decimal_places = 2)
