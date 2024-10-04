from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class PostModel(models.Model):
    user = models.CharField(max_length=20)
    title = models.CharField(max_length=120)
    text = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=120)
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)