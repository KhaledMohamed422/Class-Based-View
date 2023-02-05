from django.db import models
from django.utils import timezone
from datetime import datetime    

# Create your models here.


class Post(models.Model):
    
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    image =  models.ImageField(upload_to='post-img/')
    
    def __str__(self):
        return self.title
    


   