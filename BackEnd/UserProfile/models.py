from django.db import models
from django.conf import settings
from datetime import date

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    banner = models.ImageField(upload_to='profile_banners/', blank=True, null=True)
    public_state = models.BooleanField(default=True)
    active = models.BooleanField(default=True) 

class PersonalData(models.Model):
    profile = models.ForeignKey(Profile, default=1, related_name='personal_data', on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    experience_years = models.PositiveSmallIntegerField()
    phone =  models.CharField(max_length=50)
    freeSpace = models.TextField(blank=True, null=True)
    
class ProfessionalData(models.Model):
    profile = models.ForeignKey(Profile, default=1, related_name='professional_data', on_delete=models.CASCADE)
    company = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    timeworked = models.TextField(blank=True, null=True)
    actualwork = models.BooleanField(default=False, verbose_name=("Actual work"))

class EducationalData(models.Model):
    profile = models.ForeignKey(Profile, default=1, related_name='educational_data', on_delete=models.CASCADE)
    certification = models.CharField(max_length=120)
    year = models.DateField(default=date.today)
    file = models.FileField(upload_to='certificates/', blank=True, null=True)
    
    

