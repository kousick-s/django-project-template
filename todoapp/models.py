from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class movie(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
    
class Task(models.Model):
    user=models.ForeignKey(User)
    tTitle=models.CharField(max_length=200)
    tDesc=models.CharField(max_length=200)
    tStatus=models.CharField(max_length=200)
    tAccess=models.CharField(max_length=200)
    def __unicode__(self):
        return self.tTitle