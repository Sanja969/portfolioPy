from django.db import models

class Project(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  img = models.ImageField(default='path/to/default/image.jpg')
  techologies = models.TextField()
  source = models.CharField(max_length=200)
  live = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True) 
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name
