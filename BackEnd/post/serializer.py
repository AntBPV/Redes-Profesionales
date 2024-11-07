from post.models import PostModel
from UserProfile.models import Profile
from rest_framework import serializers


class post_serializer(serializers.ModelSerializer):
    UserProfile = serializers.PrimaryKeyRelatedField(
        queryset = Profile.objects.all(),
        required = True
    )
    
    class Meta:
        model=PostModel
        fields=['id','user', 'UserProfile', 'EnterpriseProfile', 'image', 'text']