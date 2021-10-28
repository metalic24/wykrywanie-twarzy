import tkinter
import cv2
import numpy as np
import face_detec
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

#TODO zaby te okna jako tako wygladały

def w_zdjecie():
    path = filedialog.askopenfilename()
    img = face_detec.zdjecie(path)

    cv2.imshow("zamienione", img)


    window2 = Tk()
    window2.geometry("480x320")
    window2.title("zapisz obraz")
    label2 = tkinter.Label(window2,text="Czy chcesz zapisać obraz?")
    label2.pack()


    zapis = tkinter.Button(window2, text="zapisz", command= lambda : zapisz_zdj(img,window2) )
    zapis.pack()

    window2.mainloop()



def zapisz_zdj(img,window):
    #zapisanie obrazu
    cv2.imwrite(filedialog.asksaveasfilename(filetypes=(
    ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif'))), img)
    window.destroy()
    cv2.destroyAllWindows()

window = Tk()
window.geometry("480x320")
window.title("Projekt 1")
label1 = tkinter.Label(window, text="Podmiana Twarzy")
label1.pack()
button_camera = Button(window, text="Zamiana twarzy live", command=face_detec.camera)
button_camera.pack()

button_zdjecie = Button(window, text="Zamiana twarzy ze zdjecia", command=w_zdjecie)
button_zdjecie.pack()

label2 = tkinter.Label(window, text="Neuronowy transfer stylów ")
label2.pack()
button_neuronowy = Button(window, text="Załaduj zdjęcia")
button_neuronowy.pack()

window.mainloop()
