from django.db import models

# Create your models here.
class food_table(models.Model):
  items=models.CharField(max_length=200)
  description=models.CharField(max_length=200)
  price=models.IntegerField()