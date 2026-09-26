from django.db import models 


# Create your models here.

class Student_model(models.Model):
  name = models.CharField(max_length=10)
  age = models.IntegerField()
  address = models.TextField(blank=True)

  def __str__(self)-> str:
    return self.name



class Product(models.Model):
  product_name = models.CharField(max_length=250)
  product_description = models.TextField(blank=True)
  product_image = models.FileField(upload_to='product/')
  
  def __str__(self) -> str:
    return self.product_name
  



class ToDoList(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name




class Item(models.Model):
  todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
  text = models.TextField()
  is_complete = models.BooleanField()

  def __str__(self):
      return self.text  
