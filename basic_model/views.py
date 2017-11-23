from site import _Printer

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
import random
import os
from django.core.files import File

from .models import Mnistimage

# Create your views here.

def home(request):
    return render(request, 'basic_model/home.html')


def mnisthome(request):
    return render(request, 'basic_model/mnist.html')

def mnist(request):
    mnistimage_total = Mnistimage.objects.all().count()
    random_index = int(random.random()*mnistimage_total+1)
    mnistimage = Mnistimage.objects.all()[random_index-1]
    print(mnistimage_total,random_index)
    return render(request, 'basic_model/mnist.html', {"mnistimage" : mnistimage})

def setlabel(request):
     return HttpResponse("thanx")

def registerimage(request):
    base_path = 'basic_model/static/MNIST_images/'
    for filename in os.listdir(base_path):
        mnistimage = Mnistimage()
        mnistimage.image.save(filename, File(open('basic_model/static/MNIST_images/%s' % filename, 'wb')))  # os.path.basename(base_path)
#        mnistimage.image = '/media/mahdi/fa95ce70-3a4a-4ce2-bf2a-14ed67604caf/computer_training/django/AIresearch/AIresearch1/basic_model/static/MNIST_images/%s' %filename
        mnistimage.save
    return HttpResponse(mnistimage.image) #"the image registered in the db")

def train():
    num = Mnistimage.objects.all().count()
    image_list = [Mnistimage.objects.all()[i].image for i in range(num)]
    pred_list = [Mnistimage.objects.all()[i].trained_label for i in range(num)]
    return image_list


