from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(default=17)
    phone=models.CharField(max_length=10)
    city=models.TextField()

    def __str__(self):
        return self.name
