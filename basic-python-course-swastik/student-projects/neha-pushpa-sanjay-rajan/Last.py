from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter
from PIL import ImageChops
import tkinter as tk


def original():
    img1=Image.open("image.jpg")
    img1.show()
def crop ():
    img1=Image.open("image.jpg")
    left=150
    top=33
    right=350
    bottom=300
    img2=img1.crop((left,top,right,bottom))
    img2.show()
    img2.save("crop_image.png")

def grey():
    img4=Image.open("image.jpg").convert('L')
    img4.show()
    img4.save("new_image.png")

def invert():
    emage=Image.open("image.jpg").convert('L')
    img5= ImageOps.invert(emage)
    img5.show()
    img5.save("Invert.png") 

def rotation():
    img1=Image.open("image.jpg")
    Rotate2=img1.rotate(30,expand='True')
    Rotate3=img1.rotate(90,expand='True')
    Rotate4=img1.rotate(180)
    Rotate=img1.rotate(360)
    Rotate2.show()
    Rotate3.show()
    Rotate4.show()
    Rotate.show()
    Rotate2.save("45.png")
    Rotate3.save("90.png")
    Rotate4.save("180.png")
    Rotate.save("360.png")

def blur():
    imgs2=Image.open("image.jpg").filter(ImageFilter.GaussianBlur(radius = 10))
    imgs2.show()
    imgs2.save("Blur.png")


def sharp():
    img6= Image.open("image.jpg").filter(ImageFilter.SHARPEN)  
    img7= img6.filter(ImageFilter.SHARPEN)
    img7.show()
    img7.save("sharp2.png")

def imageadd():
    img11=Image.open("image.jpg")
    img12=Image.open("u.jpg")
    img11.show()
    img12.show()
    img111=ImageChops.add_modulo(img11, img12)
    img101=ImageChops.add(img11, img12,4,8)
    img111.show()
    img101.show()
    img111.save("clip_image.png")
    img101.save("wcliping_image.png")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

Original = tk.Button(frame, 
                   text="Orginal Image", 
                   command=original)
Original.pack(side=tk.TOP)

Crop= tk.Button(frame,
                   text="crop image",
                   command=crop)
Crop.pack(side=tk.RIGHT)

Grey= tk.Button(frame,
                   text="Grey image",
                   command=grey)
Grey.pack(side=tk.TOP)


invert= tk.Button(frame,
                   text="Invert image",
                   command=invert)
invert.pack(side=tk.RIGHT)


Rotation= tk.Button(frame,
                   text="Rotate image",
                   command=rotation)
Rotation.pack(side=tk.TOP)


Blur = tk.Button(frame, 
                   text="blur Image", 
                   command=blur)
Blur.pack(side=tk.RIGHT)


Sharp= tk.Button(frame,
                   text="Sharp image",
                   command=sharp)
Sharp.pack(side=tk.TOP)


Add = tk.Button(frame, 
                   text="Addition of  Image", 
                   command=imageadd)
Add.pack(side=tk.TOP)
root.mainloop()


