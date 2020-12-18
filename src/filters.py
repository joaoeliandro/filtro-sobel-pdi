from PIL import Image, ImageFilter
import open as openImage

def imageFiltered():
  image = openImage.getImage("woman.jpg")
  imageFiltered = image.filter(ImageFilter.BLUR)

  openImage.showVertical(image, imageFiltered)

imageFiltered()