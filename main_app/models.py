from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

READINGS = (
    ('Y', 'Yeah'),
    ('N', 'Nah')
)

class Genre(models.Model):
  name = models.CharField(max_length=50)
  

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('genres_detail', kwargs={'pk': self.id})

class Comic(models.Model):
    name = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    year = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'comic_id': self.id})

    def read_for_today(self):
        return self.reading_set.filter(date=date.today()).count() >= len(READINGS)

class Reading(models.Model):
    date = models.DateField('read date')
    read = models.CharField(
        max_length=1, 
        choices=READINGS, 
        default=READINGS[0][0]
    )

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_read_display()} on {self.date}"

    class Meta:
        ordering = ['-date']