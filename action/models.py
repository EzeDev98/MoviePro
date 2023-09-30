from django.db import models
from datetime import datetime

# Create your models here

class Action(models.Model):
    year_choice = []
    for r in range(1000, (datetime.now().year+1)):
        year_choice.append((r,r))
    
    title = models.CharField(max_length=100, default="title")
    origin = models.CharField(max_length=100, default="origin")
    genre = models.CharField(max_length=100, default="genre")
    category = models.CharField(max_length=100, default="action")
    category_1 = models.CharField(max_length=100, default="action")
    category_2 = models.CharField(max_length=100, default="action")
    category_3 = models.CharField(max_length=100, default="action")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    year = models.IntegerField(('year'), choices=year_choice)
    director = models.CharField(max_length=250, default="director")
    writer = models.CharField(max_length=250, default="writer")
    stars = models.CharField(max_length=250, default="stars")
    features = models.CharField(max_length=250, default="features")
    time = models.CharField(max_length=100, default="time")
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title
