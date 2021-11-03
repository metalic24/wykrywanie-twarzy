import tkinter
import cv2
import face_detec
import  neuronowe
from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog

window = Tk()
label = tkinter.Label(window)



#okno do zjecia
def w_zdjecie():
    path = filedialog.askopenfilename()
    img = face_detec.zdjecie(path)

    cv2.imshow("zamienione", img)


    window2 = Tk()
    window2.geometry("480x320")
    window2.title("zapisz obraz")
    label2 = tkinter.Label(window2,text="Czy chcesz zapisać obraz?")
    label2.pack()


    zapis = tkinter.Button(window2, text="tak", command= lambda : zapisz_zdj(img,window2) )
    zapis.pack()

    nie_zapis = tkinter.Button(window2, text="nie", command=window2.destroy)
    nie_zapis.pack()


    window2.mainloop()

def neuronowe_zdj():
    path1 = filedialog.askopenfilename()
    path2 = filedialog.askopenfilename()
    img =  neuronowe.neuronowe_przetwarzarzanie(path1, path2)

    #img.save("/temp/temp.jpg",".JPG")







#zapis zdjecia w wybranym formacie (jako że wcześniej otwieraliśmy zdjęcie w jakimś folderze, to automatyznie przeniesie nas do tego folderu)
def zapisz_zdj(img,window):
    #zapisanie obrazu
    cv2.imwrite(filedialog.asksaveasfilename(filetypes=(
    ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif'))), img)
    window.destroy()




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
