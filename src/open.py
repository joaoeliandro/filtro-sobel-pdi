from PIL import Image
import os

IMAGE_FOLDER = "images"
OUTPUT_FOLDER = "output"

def in_path(filename):
  return os.path.join(IMAGE_FOLDER, filename)

def getImage(filename):
  image = Image.open(in_path(filename))
  return image

def showImage(image):
  imageToShow = image
  imageToShow.show()
