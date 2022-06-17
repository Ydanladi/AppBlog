from django.db import models

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Created_Date = models.DateTimeField()
    Published_Date = models.DateTimeField()
    
    def __str__(self):
        return self.Title
    
    
class post2(models.Model):
    Author = models.ForeignKey(Post, on_delete=models.CASCADE)
    

    
    
    
    
