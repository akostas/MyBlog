from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # Return to the latest created post
        # return reverse('details', args=(str(self.id)))
        # Return to the homepage
        return reverse('home')