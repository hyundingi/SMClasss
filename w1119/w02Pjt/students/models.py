from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=100)
  major = models.CharField(max_length=100)
  grade = models.IntegerField(default=1)
  age = models.IntegerField(default=1)
  gender = models.CharField(max_length=30)
  hobby = models.CharField(max_length=100)

  def __str__(self):
    return self.name