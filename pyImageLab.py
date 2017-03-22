from filtersFile import*
import os, sys
from tkinter import*
import tkinter.filedialog
import tkinter.colorchooser
from copy import copy
from PIL import Image, ImageTk,ImageFilter,ImageOps


window_size= "640x480"      #Tamaño de la ventana del programa.
size = 256, 256             #Tamaño de las miniaturas de las imágenes.
color = "grey"
filters = {'Invertir color', 'Normal','Escala de grises','Negativo'}      #ComboBox: Filtros
root = tkinter.Tk()
root.title("pyImageLab")
tkvar = StringVar(root)
tkvar.set('Invertir color')

# Método que se utiliza para cargar una imagen al programa.
def chooseImage():
    global acI
    filename =tkinter.filedialog.askopenfilename()
    inImage2 = Image.open(filename)				#Abrir Imagen
    acI = copy(inImage2)
    refreshImages(inImage2,panel)
   
#Método encargado de guardar la imagen procesada.
def saveImage():
    global outI
    savefile = tkinter.filedialog.asksaveasfile(mode='w',defaultextension=".jpg")
    if savefile:    #Comprueba si se le dío a cancelar.
        outI.save(savefile)

#Método encargado de aplicar los filtros.
def aplyFilter():
    global acI
    global outI
    auxiliarImg = copy(acI)
    filter = tkvar.get()
    if filter == 'Invertir color' :
        showIm = ImageOps.invert(auxiliarImg)
        refreshImages(showIm,panel2)
    elif filter == 'Normal':
        showIm =copy(acI)
        refreshImages(showIm,panel2)
    elif filter == 'Escala de grises':
        showIm = acI.convert("L")
        refreshImages(showIm,panel2)
    elif filter == 'Negativo':
        showIm = negativeImage(auxiliarImg)
        refreshImages(showIm,panel2)


#Método que recoge el color especificado en el botón.
def getColor():
    global color
    color = tkinter.colorchooser.askcolor()
    colorButton.configure(bg=color[1])

def aplyColorFilter():
    global color
    global acI
    global outI
    showImg = copy(acI)
    showImg = aplyColor(showImg,color)
    refreshImages(showImg,panel2)
    
def refreshImages(newMiniatureImage,panel):
    outI=copy(newMiniatureImage)
    newMiniatureImage.thumbnail(size, Image.ANTIALIAS)
    tkimageout = ImageTk.PhotoImage(newMiniatureImage)			#Mostrar imagen
    panel.configure(image = tkimageout)
    panel.image = tkimageout
            

root.geometry(window_size)
window = tkinter.Frame(root)
window.pack()
inImage = Image.open("Imagenes/intro.jpg")                      #Abrir Imagen por defecto de la entrada.
acI = copy(inImage)
outI = copy(inImage)
inImage.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
tkimage = ImageTk.PhotoImage(inImage)			#Mostrar imagen
panel = tkinter.Label(window, image=tkimage,width=256,height=256)
panel.grid(row=0)

outputimage = Image.open("Imagenes/result.jpg")			#Abrir Imagen por defecto de la salida.
outputimage.thumbnail(size, Image.ANTIALIAS)		#Cambia el tamaño de la imagen
tkimageout = ImageTk.PhotoImage(outputimage)
panel2 = tkinter.Label(window, image=tkimageout,width=256,height=256)
panel2.grid(row=0,column=2)

chooseButton = tkinter.Button(window,text="Selecionar Imagen",command=chooseImage).grid(row=1,column=0,pady=8)      #Botón de carga de imágenes
saveButton = tkinter.Button(window,text="Guadar Imagen",command=saveImage).grid(row=1,column=2)                     #Botón para guardar imágenes

Label(window,text="Seleccione filtro: ").grid(row=2,column=0)
filterMenu = OptionMenu(window,tkvar,*filters).grid(row=2,column=1)                                                 #ComboBox
filerButton = tkinter.Button(window,text="Aplicar Filtro",command=aplyFilter).grid(row=2,column=2,pady= 30)         #Botón que aplica el filtro seleccionado por el ComboBox

Label(window,text="Seleccione color del filtro: ").grid(row=3,column=0)
colorButton = tkinter.Button(window,text="Color",command=getColor,bg = "white")
colorButton.grid(row=3,column=1)
AplyColorFilterButton = tkinter.Button(window,text="Aplicar color",command=aplyColorFilter).grid(row=3,column=2)

root.mainloop()
