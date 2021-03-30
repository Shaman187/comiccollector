from django.db import models

# Create your models here.

class Comic(models.Model):
    name = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    
    def __str__(self):
        return self.name