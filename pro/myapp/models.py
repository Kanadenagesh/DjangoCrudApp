from django.db import models

# Create your models here.
class student(models.Model):
 name = models.CharField(max_length=80)
 age =models.IntegerField()
 city = models.CharField(max_length=40)
 
 def __str__(self):
  return self.name
