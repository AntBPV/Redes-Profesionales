from post.models import PostModel
from rest_framework import serializers

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model=PostModel
        fields=['id','user','title','text']