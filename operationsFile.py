# -*- encoding: utf-8 -*-
from copy import copy
from PIL import Image, ImageTk,ImageFilter,ImageOps
#Invierte Imagen(arriba abajo)
def imageGyro(image):
    aux = copy(image)
    width, height = image.size
    for i in range(width):
        for j in range(height):
            r,g,b = aux.getpixel((i,j))
            image.putpixel((i,(height-1)-j),(r,g,b))
    return image

#Invierte Imagen (izquierda derecha)
def imageInverter(image):
    aux = copy(image)
    width, height = image.size
    for i in range(width):
        for j in range(height):
            r,g,b = aux.getpixel((i,j))
            image.putpixel(((width-1)-i,j),(r,g,b))
    return image

#Image Duplicater
def imageDuplicater(image):
    aux = copy(image)
    width, height = image.size
    for i in range(width):
        for j in range(height):
            if i%2 == 1:
                r,g,b = aux.getpixel((i,j))
                image.putpixel(((width-1)-i,j),(r,g,b))
    return image

#Disminuir Tamaño
def newSize(image):
    image.thumbnail((150,150), Image.ANTIALIAS)		#Cambia el tamaño de la imagen
    return image
