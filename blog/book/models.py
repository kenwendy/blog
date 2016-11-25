from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=128, unique=True)
    author = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    pubDate = models.DateTimeField(auto_now_add=True)
    version = models.IntegerField(default=1)
    price = models.IntegerField()
    
    def __str__(self):
        return self.title