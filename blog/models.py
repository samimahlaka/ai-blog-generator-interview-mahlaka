from django.db import models

# Create your models here.
class Blog(models.Model):
    key_word = models.TextField()
    blog = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.key_word}"