from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import EnterpriseProfile
from .serializer import EnterpriseProfileSerializer

class EnterpriseProfileApiView(APIView):
    # Get method will return a single profile or a list of all e-profiles
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            # If it gets a primary key, it will return a single profile
            profile = EnterpriseProfile.objects.get(id=pk, active=True)
            serializer = EnterpriseProfileSerializer(profile)
        else:
            # Else, it will return a list of all profiles
            profiles = EnterpriseProfile.objects.filter(active=True)
            serializer = EnterpriseProfileSerializer(profiles, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = {
            'user': request.data.get('user'),
            'name': request.data.get('name'),
            'backstory': request.data.get('backstory'),
            'picture': request.data.get('picture'),
            'banner': request.data.get('banner'),
            'company_data': request.data.get('company_data')
        }
        serializer = EnterpriseProfileSerializer(data=data)
        
        # Validate the data and return the correct response
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return a bad request if the data is invalid
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        myProfile = EnterpriseProfile.objects.get(id=pk, active=True)
        serializer = EnterpriseProfileSerializer(myProfile, data=request.data, partial=True)
        
        # Same validation as the post method
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        # Delete method doesn't actually delete the profile
        # It just sets the active and public fields to False
        profile_to_delete = EnterpriseProfile.objects.get(id=pk)
        profile_to_delete.active = False
        profile_to_delete.public_state = False
        profile_to_delete.save()
        return Response(status=status.HTTP_204_NO_CONTENT)