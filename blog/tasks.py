from .cohere_client import generate_blog_content
from .models import Blog
from celery import shared_task
 
@shared_task
def generate_blog_task(key_word):
    blog = generate_blog_content(key_word)
    Blog.objects.create(key_word = key_word , blog = blog)
     