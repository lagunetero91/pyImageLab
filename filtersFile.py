# -*- encoding: utf-8 -*-

#Método que pone la imágen en negativo.       
def negativeImage(aux):
    width, height = aux.size
    for i in range(width):
        for j in range(height):
            r, g, b = aux.getpixel((i,j))
            aux.putpixel((i,j),(255-r,255-g,255-b))
    return aux

#Método encargado de aplicar el filtro de color a la imágen.
def aplyColor(image,color):
	nr,ng,nb = color[0]
	width, height = image.size
	image.convert("L")
	for i in range(width):
		for j in range(height):
			r, g, b = image.getpixel((i,j))
			media =(r+g+b)/3
			if media < 128:
				image.putpixel((i,j),((int)(nr*media/128),(int)(ng*media/128),(int)(nb*media/128)))
			else:
				image.putpixel((i,j),((int)(nr+(255-nr)*(media-128)/128),(int)(ng+(255-ng)*(media-128)/128),(int)(nb+(255-nb)*(media-128)/128)))
	return image