from django.db import models

# Create your models here.

class Library(models.Model):
    b_name = models.CharField(max_length=100)
    b_title = models.CharField(max_length=300)
    b_author = models.CharField(max_length=50)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.b_name