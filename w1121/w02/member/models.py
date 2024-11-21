from django.db import models

# Create your models here.
class Member(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  nicname = models.CharField(max_length=100)

  def __str__(self):
    return self.name