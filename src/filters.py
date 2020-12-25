from PIL import Image, ImageFilter
import open as openImage

def imageFiltered(filename):
  image = openImage.getImage(filename)
  imageFiltered = image.filter(ImageFilter.BLUR)

  openImage.showVertical(image, imageFiltered)

def showBoxBlur(filename, rImage = 1):
  originalImage = openImage.getImage(filename)
  imageFiltered = originalImage.filter(ImageFilter.BoxBlur(rImage))

  imageHorizontal = openImage.showHorizontal(originalImage, imageFiltered)
  openImage.saveImage(imageHorizontal, '{}_boxblur_{}.png'
    .format(filename[:filename.index('.')], rImage))
  
def showVertica(filename, rImage = 1):
  originalImage = openImage.getImage(filename)
  imageFiltered = originalImage.filter(ImageFilter.BoxBlur(rImage))

  imageHorizontal = openImage.showHorizontal(originalImage, imageFiltered)
  openImage.saveImage(imageHorizontal, '{}_boxblur_{}.png'
    .format(filename[:filename.index('.')], rImage))
  
if __name__ == "__main__":
  show_box_blur("lenna.png", 4)