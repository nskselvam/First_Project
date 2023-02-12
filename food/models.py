from django.db import models
from datetime import datetime


# Create your models here.
class food_table(models.Model):
  items=models.CharField(max_length=200)
  description=models.CharField(max_length=200)
  price=models.IntegerField()
  Img_items=models.CharField(max_length=500,default='https://images.unsplash.com/photo-1671221464173-823f79579e31?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80')
  contact_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self): 
    return self.description
  