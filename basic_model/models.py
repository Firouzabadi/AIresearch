from django.db import models
import pandas as pd
from math import pi
# Create your models here.

class Mnistimage(models.Model):
    label_choice = [(1,'even'),(2,'odd'),(3,'Null')]

    imageid = models.AutoField(primary_key=True)
    trained_label = models.IntegerField(choices=label_choice, null= False, default=3)
    predicted_label = models.IntegerField(choices=label_choice, null= False, default=3)
    image = models.ImageField(upload_to = 'MNIST_images', default='MNIST_images/one_1.png',null=True)

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField


#superuser pass:pass12345678 user:admin ho