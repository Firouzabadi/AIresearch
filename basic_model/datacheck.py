from .models import Mnistimage

def trainedFiles():
    trainedObjects = Mnistimage.objects.filter(trained_label=3)
    trainedObjectsFiles = trainedObjects.values('image')

    return (trainedObjectsFiles)
