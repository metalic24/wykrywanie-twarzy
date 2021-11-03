import tkinter

import PIL
import cv2
import face_detec
import  neuronowe
import  numpy as np
from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog

window = Tk()
global label
global button_zapis
label = tkinter.Label(window)
button_zapis = tkinter.Button(window)
img = None



#okno do zjecia
def w_zdjecie():
    flaga = 1
    path = filedialog.askopenfilename()
    img = face_detec.zdjecie(path)
    image = img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (500, 500))
    img = ImageTk.PhotoImage(image=PIL.Image.fromarray(img))

    label.config(image=img)
    label.image = img
    label.pack()

    button_zapis.configure(text = "Zapisz zdjęcie z podmienioną twarzą",command = lambda: zapisz_zdj(image,flaga))
    button_zapis.pack()




def neuronowe_zdj():
    flaga = 2
    path1 = filedialog.askopenfilename()
    path2 = filedialog.askopenfilename()
    img =  neuronowe.neuronowe_przetwarzarzanie(path1, path2)
    image=img




    img = ImageTk.PhotoImage(image=img)

    label.config(image=img)
    label.image = img
    label.pack()
    button_zapis.configure(text="Zapisz zdjęcie neuronowego transferu stylów", command=lambda: zapisz_zdj(image, flaga))
    button_zapis.pack()





#zapis zdjecia w wybranym formacie (jako że wcześniej otwieraliśmy zdjęcie w jakimś folderze, to automatyznie przeniesie nas do tego folderu)
def zapisz_zdj(img,flaga):

    path=filedialog.asksaveasfilename(filetypes=(
        ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif')), defaultextension=".jpg")

    #zapisanie obrazu
    if flaga == 1:

        cv2.imwrite(path, img)

    if flaga == 2:
        img.save(path)






#otwarcie programu

window.geometry("1000x1000")
window.title("Projekt 1")
label1 = tkinter.Label(window, text="Podmiana Twarzy")
label1.pack()
button_camera = Button(window, text="Zamiana twarzy live", command=face_detec.camera)
button_camera.pack()

button_zdjecie = Button(window, text="Zamiana twarzy ze zdjecia", command=w_zdjecie)
button_zdjecie.pack()

label2 = tkinter.Label(window, text="Neuronowy transfer stylów ")
label2.pack()

#to jeszcze będzie dorobione
button_neuronowy = Button(window, text="Załaduj zdjęcia", command=neuronowe_zdj)
button_neuronowy.pack()

label.pack();







window.mainloop()
