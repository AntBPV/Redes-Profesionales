from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions, generics
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError

from .models import PostModel

from .serializer import post_serializer

# APIView will handle GET, POST, PUT, DELETE based on our url request

class PostApiView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        try:
            if pk:
                # Try to get a specific post
                post = PostModel.objects.get(id=pk, active=True, public_state=True)
                serializer = post_serializer(post)
            else:
                # Retrieve all active and public posts
                posts = PostModel.objects.filter(active=True, public_state=True)
                serializer = post_serializer(posts, many=True)
            return Response(serializer.data)
        
        except ObjectDoesNotExist:
            return Response(
                {"error": "Post not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request, *args, **kwargs):
        try:
            data = {
                'user': request.data.get('user'),
                'UserProfile': request.data.get('UserProfile'),
                'EnterpriseProfile': request.data.get('EnterpriseProfile'),
                'text': request.data.get('text'),
                'image': request.data.get('image'),
            }
            
            serializer = post_serializer(data=data)
            
            # Validate and save the serializer
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            # If validation fails, return specific errors
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        except ValidationError as ve:
            return Response(
                {"error": str(ve)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": "An unexpected error occurred"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def put(self, request, pk):
        try:
            # Try to get the existing post
            myPost = PostModel.objects.get(id=pk, active=True)
            
            # Attempt to update the post
            serializer = post_serializer(myPost, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            # If validation fails, return specific errors
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        except ObjectDoesNotExist:
            return Response(
                {"error": "Post not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except ValidationError as ve:
            return Response(
                {"error": str(ve)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": "An unexpected error occurred"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete(self, request, pk):
        try:
            # Try to get and soft delete the post
            post_to_delete = PostModel.objects.get(id=pk)
            post_to_delete.active = False
            post_to_delete.public_state = False
            post_to_delete.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except ObjectDoesNotExist:
            return Response(
                {"error": "Post not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": "An unexpected error occurred"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
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