from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(default=15)
    phone=models.CharField(max_length=10)
    city=models.TextField()
    date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    