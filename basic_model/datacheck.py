from .models import Mnistimage
import os

def retrieveMnist():
    mnistObjects = Mnistimage.objects.all()
    mnistImages = mnistObjects.values('image')
    mnistPrediction = mnistObjects.values('predicted_label')
    mnistTrain = mnistObjects.values('trained_label')
    return (mnistImages, mnistPrediction, mnistTrain)

def createMnist():
    for filename in os.listdir(base_path):
        mnistimage = Mnistimage()
        mnistimage.image.save(filename, File(open('basic_model/static/MNIST_images/%s' % filename, 'wb')))

    pass