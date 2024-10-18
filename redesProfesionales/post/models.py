from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Making user
User = settings.AUTH_USER_MODEL

#TODO: remove title field, as it is not needed
class PostModel(models.Model):
    user = models.ForeignKey(User, default=1, null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)