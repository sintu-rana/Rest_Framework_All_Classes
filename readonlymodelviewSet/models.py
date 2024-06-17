from django.db import models

# Create your models here.

class Collage(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=20, null=True, blank=True)
    phone=models.CharField(max_length=10)
    location=models.TextField()
    date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    