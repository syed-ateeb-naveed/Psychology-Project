from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CIVIL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('relationship', 'In a Relationship'),
    ]
    civil_status = models.CharField(max_length=20, choices=CIVIL_STATUS_CHOICES)
    occupation = models.CharField(max_length=100)
    place_of_residence = models.CharField(max_length=400)
    cellphone = models.BigIntegerField()
    SCHOOL_LEVEL_CHOICES = [
        ('elementary', 'Elementary/junior school'),
        ('high_school', 'High School'),
        ('bachelour', 'Bachelor’s degree'),
        ('master', 'Master'),
    ]
    level_of_school = models.CharField(max_length=20, choices=SCHOOL_LEVEL_CHOICES)