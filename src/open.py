from PIL import Image
import numpy as np
import os

INPUT_DIR_IMAGE = "images"
OUTPUT_DIR_IMAGE = os.path.join("images", "output")

def in_path(filename):
  return os.path.join(INPUT_DIR_IMAGE, filename)

def getImage(filename):
  image = Image.open(in_path(filename))
  return image

def saveImage(file, filename):
  dir = os.path.join(OUTPUT_DIR_IMAGE, filename)
  file.save(dir)

def showImage(image):
  imageToShow = image
  imageToShow.show()

def showVertical(image1, image2):
  imageVertical = Image.fromarray(np.vstack((np.array(image1), np.array(image2))))
  imageVertical.show()

  return imageVertical