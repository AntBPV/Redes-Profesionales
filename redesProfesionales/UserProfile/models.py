from django.db import models
from django.conf import settings
from datetime import date

User = settings.AUTH_USER_MODEL

class PersonalData(models.Model):
    age = models.PositiveSmallIntegerField()
    phone =  models.CharField(max_length=50)
    experience_years = models.PositiveSmallIntegerField()
    freeSpace = models.TextField(blank=True, null=True)

class ProfessionalData(models.Model):
    enterprise = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    timeworked = models.TextField(blank=True, null=True)
    actualwork = models.BooleanField(default=False, verbose_name=("Actual work"))

class EducationalData(models.Model):
    school = models.CharField(max_length=120)
    certification = models.CharField(max_length=120)
    year = models.DateField(default=date.today)
    
class Profile(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete = models.SET_NULL, db_constraint=True)
    name = models.CharField(max_length=120)
    personal_data = models.ForeignKey(PersonalData, on_delete = models.CASCADE, related_name="profile", db_constraint = True)
    professional_data = models.ForeignKey(ProfessionalData, on_delete = models.CASCADE, related_name="profile", db_constraint=True)
    educational_data = models.ForeignKey(EducationalData, on_delete = models.CASCADE, related_name="profile", db_constraint=True)
    active = models.BooleanField(default=True)
