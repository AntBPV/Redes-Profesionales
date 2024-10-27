from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView

from .models import Profile
from .serializer import ProfileSerializer

# APIView will handle GET, POST, PUT, DELETE based on our url request
class ProfileApiView(APIView):
    # Get method will return a single profile or a list of all profiles
    def get(self,request, pk=None, *args, **kwargs):
        # If it gets a primary key, it will return a single profile
        if pk:
            profile = Profile.objects.get(id=pk, active=True)
            serializer = ProfileSerializer(profile)
        # If it doesn't get a primary key, it will return a list of all profiles
        else:
            profiles = Profile.objects.filter(active = True)
            serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    # Post method will create a new profile
    def post(self,request,*args,**kwargs):
        data = {
            'user': request.data.get('user'),
            'name': request.data.get('name'),
            'personal_data': request.data.get('personal_data'),
            'professional_data': request.data.get('professional_data'),
            'educational_data': request.data.get('educational_data'),
        }
        serializer = ProfileSerializer(data=data)
        
        # This will validate the data and return the correct response
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, it will return an error
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    # Put method will update an existing profile
    def put(self, request, pk):
        myPost = Profile.objects.get(id=pk,active=True)
        serializer = ProfileSerializer(myPost, data=request.data)
        
        # Similar validation as the post method
        # This will validate the data and return the correct response
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # If the data is invalid, it will return an error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete method doesn't actually delete the profile
    # It just sets the active field to False
    def delete(self,request, pk):
        profile_to_delete = Profile.objects.get(id=pk)
        profile_to_delete.active = False
        profile_to_delete.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    