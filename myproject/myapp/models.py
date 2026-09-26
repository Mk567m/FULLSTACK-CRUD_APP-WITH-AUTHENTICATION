from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.CharField()
  grade = models.IntegerField()
  age= models.IntegerField(default=5)
  address = models.CharField()
  email = models.EmailField()
  

class employee(models.Model):
  name = models.CharField()
  age= models.IntegerField(default=5)
  address = models.CharField()
  email = models.EmailField()
  phone_number = models.IntegerField()
  salary = models.IntegerField()
  job = models.CharField(null=True, blank=False)
  experience = models.IntegerField()

class Car(models.Model):
  carname = models.CharField()   
  model = models.CharField()
  price = models.IntegerField()
  year = models.IntegerField()
  origin = models.CharField()


  def __str__(self) -> str:
    return self.carname
  


  def __str__(self):
    return self.name  



