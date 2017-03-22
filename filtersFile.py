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

# Transforma imágen RGB a HSV
def rgb2hsvImage(image):
    width, height = image.size
    for i in range(width):
        for j in range(height):
            r,g,b = image.getpixel((i,j))
            h,s,v = rgb2hsvPixel(r,g,b)
            image.putpixel((i,j),((int)(h),(int)(s),(int)(v)))
    return image

#Convertir pixel RGB a HSV
def rgb2hsvPixel(r,g,b):
    mx = max(r,g,b)
    mn = min(r,g,b)
    df = mx - mn
    if mx == mn :
        h=0
    elif mx == r:
        h = 60*(((g-b)/df)+360)
    elif mx == g:
        h = 60*(((b-r)/df)+120)
    elif mx == b:
        h = 60*(((r-g)/df)+240)

    if mx == 0:
        s = 0
    else:
        s = 1 - mn/mx

    v = mx
    return v,h,s
    print("hola")
