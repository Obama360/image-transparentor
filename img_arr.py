import numpy as np
from PIL import Image

color = [255,255,255] #rgb value
tolerance = 120 #between 0 and 255
replace = [0,0,0,0] #rgba value for png, rgb for jpg

imagepath="C:\\Users\\802042\\Pictures\\python\\original.png"
print("opening image...")
img = Image.open(imagepath, 'r')
height, width = img.size
print("Height: {}, Width: {}".format(height, width))
print("converting into array...")
pixels = np.array(img)

print("processing image...")
for y in range(height):
    for x in range(width):
        try:
            if ((color[0] - tolerance < pixels[x][y][0] < color[0] + tolerance) and (color[1] - tolerance < pixels[x][y][1] < color[1] + tolerance) and (color[2] - tolerance < pixels[x][y][2] < color[2] + tolerance)):
                pixels[x][y] = replace
                #print("x = {}, y = {}, color = {}".format(x, y, pixels[x][y]))
        except:
             print("No pixel found at x={} y={}".format(x, y))

print("saving file...")
result = Image.fromarray(pixels)
result.save("C:\\Users\\802042\\Pictures\\python\\result.png")
print("all done!")
