from mcpi.minecraft import Minecraft
from mcpi import block
from   time import sleep
import random
from PIL import Image
import matplotlib.pyplot as plt
import math
colours = [ (255, 255, 255, "00"),
            (255, 0, 0, "14"),
            (255, 128, 0, "01"),
            (0, 255, 0, "13"),
            (255,128,255,"02"),
            (50,50,255,"03"),
            (255,255,0,"04"),
            (50,255,50,"05"),
            (255,102,178,"06"),
            (96,96,96,"07"),
            (192,192,192,"08"),
            (0,200,200,"09"),
            (150,0,150,"10"),
            (0,0,255,"11"),
            (102,51,0,"12"),
            (0,0,0,"15")]
            


def nearest_colour( subjects, query ):
    return min(subjects,key = lambda subject:sum((s - q) ** 2 for s,q in zip( subject, query ) ) )


#print( nearest_colour( colours, (64, 0, 0) ) ) # dark red
#print( nearest_colour( colours, (0, 192, 0) ) ) # green
#print( nearest_colour( colours, (255, 255, 64) ) ) # white

def init():
	#ipString = "127.0.0.1"
	ipString = "192.168.7.226"
	#mc = Minecraft.create("127.0.0.1", 4711)
	mc = Minecraft.create(ipString, 4711)
	mc.setting("world_immutable",False)
	#x, y, z = mc.player.getPos()  
	return mc
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'png')

# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel
    
def main():
	mc = init()
	lst=[]
	#img=open_image("loss.png")
	#img =create_image(10,10)
	x,y,z=mc.player.getPos()
	
	#plt.imshow(img);
	selection=input("what is the name of your file? must contain the extension: ")
	img = Image.open(selection);
	img=img.convert('RGB')
	px=img.load()
	#plt.show();
	for i in range(0,img.width):
		for j in range(0,img.height):
			coord=(-i,abs(img.height-1-j))
			bloop=(img.getpixel(coord))
			print(bloop)
			woolcolor=str(nearest_colour(colours, bloop))
			#print(woolcolor)
			woolcolor=(woolcolor[-4:])
			woolcolor=(woolcolor[:2])
			print(woolcolor)
			#lst.append(woolcolor)
			mc.setBlock(x+5+i,y+j,z,35,int(woolcolor))
			#print(nearest_colour(colours, px[i,j]))
	#print(lst)		
	print(img.size)
	

if __name__ == "__main__":
 main()

