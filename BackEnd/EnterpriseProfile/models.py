from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class EnterpriseProfile(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    backstory = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    banner = models.ImageField(upload_to='profile_banners/', blank=True, null=True)
    active = models.BooleanField(default=True)
    
class CompanyData(models.Model):
    enterprise = models.ForeignKey(EnterpriseProfile, default=1, related_name='company_data', on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    foundationDate = models.CharField(max_length=60)
    workers = models.PositiveIntegerField()
    field = models.CharField(max_length=120)
    