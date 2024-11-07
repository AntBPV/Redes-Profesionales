from django.db import models
from django.conf import settings
from django.utils.text import slugify
from UserProfile.models import Profile
from EnterpriseProfile.models import EnterpriseProfile

# Making user
User = settings.AUTH_USER_MODEL

class PostModel(models.Model):
    user = models.ForeignKey(User, default=1, null=True,on_delete=models.SET_NULL)
    UserProfile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    EnterpriseProfile = models.ForeignKey(EnterpriseProfile, null = True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='posts_image/', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    public_state = models.BooleanField(default=True)
    active = models.BooleanField(default=True)