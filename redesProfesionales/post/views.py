from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions, generics

from .models import PostModel

from .serializer import post_serializer

# APIView will handle GET, POST, PUT, DELETE based on our url request
class PostApiView(APIView):
    
    # Get method, returns a list or a single post
    def get(self,request, pk=None, *args, **kwargs):
        # If it gets a primary key, it will return a single post
        if pk:
            post = PostModel.objects.get(id=pk, active=True, public_state=True)
            serializer = post_serializer(post)
        # If it doesn't get a primary key, it will return a list of all posts
        else:
            posts = PostModel.objects.filter(active = True, public_state = True)
            serializer = post_serializer(posts, many=True)
        return Response(serializer.data)
    
    # Post method doesn't require a primary key
    # Post method will create a new post
    def post(self,request,*args,**kwargs):
        data = {
            'user': request.data.get('user'),
            'image': request.data.get('image'),
            'text': request.data.get('text'),
        }
        serializer = post_serializer(data=data)
        
        # This will validate the data and return the correct response
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If the data is invalid, it will return an error
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    # Puf method will update existing posts by getting a primary key
    def put(self, request, pk):
        myPost = PostModel.objects.get(id=pk,active=True)
        serializer = post_serializer(myPost, data=request.data)
        
        # Similar validation as the post method
        # This will validate the data and return the correct response
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # If the data is invalid, it will return an error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete method doesn't actually delete
    # It just sets the active field to false
    def delete(self,request, pk):
        post_to_delete = PostModel.objects.get(id=pk)
        post_to_delete.active = False
        post_to_delete.public_state = False
        post_to_delete.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PostApiPrivateView(APIView):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            posts = PostModel.objects.filter(user = request.user, active=True)
            if(posts is not None):
                serializer = post_serializer(posts, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)    

class PostApiAdminView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        # If it gets a primary key, it will return a single post
        if pk:
            post = PostModel.objects.get(id=pk)
            serializer = post_serializer(post)
        # If it doesn't get a primary key, it will return a list of all posts
        else:
            posts = PostModel.objects.all()
            serializer = post_serializer(posts, many=True)
        return Response(serializer.data)