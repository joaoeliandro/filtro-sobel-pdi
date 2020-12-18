from PIL import Image
import open as openImage

def grayScale(imageColored):
  width, height = imageColored.size
  image = Image.new("RGB", (width, height))

  for x in range(width):
    for y in range(height):
      pixel = imageColored.getpixel((x, y))
      luminous = (pixel[0] + pixel[1] + pixel[2])//3

      image.putpixel((x, y), (luminous, luminous, luminous))

  return image

def grayScaleLevel(imageColored):
  width, height = imageColored.size
  image = Image.new("RGB", (width, height))

  for x in range(width):
    for y in range(height):
      pixel = imageColored.getpixel((x, y))
      luminous = int(0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2])

      image.putpixel((x, y), (luminous, luminous, luminous))

  return image

if __name__ == "__main__":
  womanImage = openImage.getImage("woman.jpg")
  
  print(womanImage.getpixel((100, 100)))
  print(womanImage.getpixel((400, 200)))
  print(womanImage.getpixel((300, 180)))

  womanGray = grayScaleLevel(womanImage)
  openImage.saveImage(womanGray, "womanGray2.jpg")
  
