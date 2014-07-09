from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class movie(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
    
class Task(models.Model):
    user=models.ForeignKey(User)
    tName=models.CharField(max_length=200)