from django.db import models 
from CrudApp.models import *
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
 
##############################################

class Product(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  product_name = models.CharField(max_length=250)
  product_description = models.TextField(blank=True)
  product_image = models.FileField(upload_to='product/')
  view_count = models.IntegerField(default=1)
  
  def __str__(self) -> str:
    return self.product_name
