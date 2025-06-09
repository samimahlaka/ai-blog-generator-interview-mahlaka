from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from .cohere_client import generate_blog_content


# Create your views here.

@api_view(['POST'])
def generate_blog(request):
    key_word = request.data.get('key_word')

    if not key_word:
        return Response({"error" : "key_word is required"} , status=status.HTTP_404_NOT_FOUND)
    
    generated_blog = generate_blog_content(key_word)
    
    data = {
        "key_word" : key_word,
        "blog" : generated_blog,
    }
    
    serializer = BlogSerializer(data = data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

