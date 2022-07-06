### Imports ###
import numpy as np
import PIL.Image
from tkinter import *
import tkinter

### Actual Image processing code ###
def ProcessImage(imagepath, color, tolerance, replace, export):
#color = [255,255,255] #rgb value
#tolerance = 120 #between 0 and 255
#replace = [0,0,0,0] #rgba value for png, rgb for jpg
#imagepath="C:\\Users\\802042\\Pictures\\python\\original.png"
    
    try:
        print("opening image {}...".format(imagepath))
        img = PIL.Image.open(imagepath, 'r')
    
        height, width = img.size
        print("Height: {}, Width: {}".format(height, width))
        print("converting into array...")
        pixels = np.array(img)

        print("processing image...")
        for y in range(height):
            for x in range(width):
                if ((color[0] - tolerance < pixels[x][y][0] < color[0] + tolerance) and (color[1] - tolerance < pixels[x][y][1] < color[1] + tolerance) and (color[2] - tolerance < pixels[x][y][2] < color[2] + tolerance)):
                    pixels[x][y] = replace
                    #print("x = {}, y = {}, color = {}".format(x, y, pixels[x][y]))

        print("saving file...")
        result = PIL.Image.fromarray(pixels)
        result.save(export)
        print("all done!")
        tkinter.messagebox.showinfo(title="Image processed", message="Image has been processed!")
        
    except:
        tkinter.messagebox.showerror(title="Failed", message="Failed to process image!")

### Form Stuff ###
form = Tk()
form.wm_geometry("300x360")
form.title("Image processor")

labelPath = Label(form, text="Image path")
labelPath.pack()
textPath = Entry(form)
textPath.pack()
textPath.focus_set()

labelOrig = Label(form, text="Color to replace (r,g,b)")
labelOrig.pack()
textOrigR = Entry(form)
textOrigR.pack()
textOrigG = Entry(form)
textOrigG.pack()
textOrigB = Entry(form)
textOrigB.pack()

labelTolerance = Label(form, text="Origin color tolerance")
labelTolerance.pack()
sliderTolerance = Scale(form, from_=0, to=255, orient='horizontal')
sliderTolerance.pack()

labelDest = Label(form, text="Replacement color (r,g,b, transparency)")
labelDest.pack()
textDestR = Entry(form)
textDestR.pack()
textDestG = Entry(form)
textDestG.pack()
textDestB = Entry(form)
textDestB.pack()
textDestA = Entry(form)
textDestA.pack()

labelSave = Label(form, text="Image export path")
labelSave.pack()
textSave = Entry(form)
textSave.pack()

def callback():
    try:
        imagepath = textPath.get()
        color = [int(textOrigR.get()), int(textOrigG.get()), int(textOrigB.get())]
        tolerance = sliderTolerance.get()
        replace = [int(textDestR.get()), int(textDestG.get()), int(textDestB.get()), int(textDestA.get())]
        export = textSave.get()
        form.destroy()
    
        ProcessImage(imagepath, color, tolerance, replace, export)
    except:
        tkinter.messagebox.showerror(title="Failed", message="One or more inputs are not allowed")
button = Button(form, text = "OK", width = 10, command = callback)
button.pack()

mainloop()
