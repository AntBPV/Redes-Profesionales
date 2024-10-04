from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions

from .models import PostModel

from .serializer import post_serializer

# Create your views here.
class PostApiView(APIView):
    def get(self,request,*args,**kwargs):
        post_list = PostModel.objects.all()
        serializer_posts = post_serializer(post_list,many=True)
        return Response(serializer_posts.data, status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        data = {
            'user': request.data.get('user'),
            'title': request.data.get('title'),
            'text': request.data.get('text'),
            'slug': request.data.get('slug')
        }
        serializer = post_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pkid):
        myPost = PostModel.objects.all(id=pkid).update(
            user = request.data.get('user'),
            title = request.data.get('title'),
            text = request.data.get('text'),
            slug = request.data.get('slug'),
        )
        return Response(myPost, status=status.HTTP_200_OK)