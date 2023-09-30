from django.db import models
from datetime import datetime

# Create your models here.
class Movie(models.Model):
    
    year_choice = []
    for r in range(1000, (datetime.now().year+1)):
        year_choice.append((r,r))
    
    title = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    category_1 = models.CharField(max_length=100)
    category_2 = models.CharField(max_length=100)
    category_3 = models.CharField(max_length=100)
    category_4 = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    year = models.IntegerField(('year'), choices=year_choice)
    director = models.CharField(max_length=250)
    writer = models.CharField(max_length=250)
    stars = models.CharField(max_length=250)
    features = models.CharField(max_length=250)
    time = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    
    
    def __str__(self):
        return self.title