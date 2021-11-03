import tkinter

import PIL
import cv2
import face_detec
import  neuronowe
from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog

window = Tk()
global label
label = tkinter.Label(window)
img = None


#okno do zjecia
def w_zdjecie():
    path = filedialog.askopenfilename()
    img = face_detec.zdjecie(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(image=PIL.Image.fromarray(img))

    label.config(image=img)
    label.image = img
    label.pack()




def neuronowe_zdj():
    path1 = filedialog.askopenfilename()
    path2 = filedialog.askopenfilename()
    img =  neuronowe.neuronowe_przetwarzarzanie(path1, path2)




    img = ImageTk.PhotoImage(image=img)

    label.config(image=img)
    label.image = img
    label.pack()







#zapis zdjecia w wybranym formacie (jako że wcześniej otwieraliśmy zdjęcie w jakimś folderze, to automatyznie przeniesie nas do tego folderu)
def zapisz_zdj(img,flaga):
    #zapisanie obrazu
    if flaga == 1:
        cv2.imwrite(filedialog.asksaveasfilename(filetypes=(
                 ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif'))), img)

    else:
        img.save(filedialog.asksaveasfilename(filetypes=(
                 ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif'))), img)





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




window.mainloop()
