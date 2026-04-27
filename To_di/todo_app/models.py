from django.db import models

# Create your models here.
class Tasks(models.Model):
  name = models.CharField(max_length=55)
  descript = models.TextField()
  date = models.DateField()
  def __str__(self):
    return self.name
  