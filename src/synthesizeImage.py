from PIL import Image
import open as openImage
import colors as color

def createImage(size, color):
  if color:
    newImage = Image.new("RGB", size, color)
  else:
    newImage = Image.new("RGB", size)

  return newImage

def triangle(size):
  triangle = createImage(size, color.WHITE)

  for x in range(size[0]):
    for y in range(size[0]):
      if x < y:
        triangle.putpixel((x, y), color.BLACK)

  return triangle

def flagFrance(height):
  width = 3*height//2
  flag = createImage((width, height), color.WHITE)

  offset = width//3

  for x in range(offset):
    for y in range(height):
      flag.putpixel((x, y), color.BLUE)
      flag.putpixel((x + 2*offset, y), color.RED)

  return flag

def flagJapan(height):
  width = 3*height//2
  rCircle = 3*height//10
  centerImage = (width//2, height//2)

  flag = createImage((width, height), color.WHITE)

  for x in range(centerImage[0]-rCircle, centerImage[0]+rCircle):
    for y in range(centerImage[1]-rCircle, centerImage[1]+rCircle):
      if (x-centerImage[0])**2 + (y-centerImage[1])**2 <= rCircle**2:
        flag.putpixel((x, y), color.DARKRED)

  return flag

if __name__ == "__main__":
  # triangle = triangle((700, 700))
  # openImage.showImage(triangle)

  # flagFrance = flagFrance(700)
  # openImage.showImage(flagFrance)

  flagJapan = flagJapan(700)
  openImage.showImage(flagJapan)
