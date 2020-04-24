import socket                                         
import time
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

work = 'True'

def close_escape(event=None):
    root.destroy()
    global work
    work = 'False'

# get local machine name
#host = '150.254.11.216'
host = '192.168.0.6'
port = 9999                                           

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# bind to the port
serversocket.bind((host, port))



#create window
root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.attributes("-fullscreen", True)
#click "Escape" to exit
root.bind("<Escape>", close_escape)
root.title("Wizualizacja satelitów na ekranie TV")
can = Canvas(root,width = w, height = h)
can.pack()

#load images to window
blue = "blue2.jpg"
background_image = ImageTk.PhotoImage(Image.open(blue))
can.create_image(0 ,0, anchor = NW, image = background_image)
can.create_text(w - 310, h - 100,
                font=("Sakkal Majalla", 24), fill = 'white', text="Praca dyplomowa inżynierska")
can.create_text(w - 480, h - 60,
                font=("Sakkal Majalla", 20), fill = 'white', text="Wykonał :")
can.create_text(w - 240, h - 60,
                font=("Sakkal Majalla", 28), fill = 'white', text="Paweł Koźmiński")
politechnika = "logo2.png"
politechnika_image = ImageTk.PhotoImage(Image.open(politechnika))
can.create_image((w / 90) , 20, anchor = NW,
                       image =  politechnika_image)
can.create_text((w / 2 + (w/6)), 80,
                font=("Sakkal Majalla bold", 24), fill = 'white',
                text="Wizualizacja  położenia satelitów GPS i GLONASS na ekranie TV")
can.create_text((w / 20), (h / 6),fill = 'white',
                text="Acutime")
screen4 = "image4.png"
img4 = Image.open(screen4)
screen_image4 = ImageTk.PhotoImage(img4)
can.create_image((w / 3) ,((h / 2)+ (h / 3) + 40),
                                   anchor = NW, image = screen_image4)
legend = "legenda1.png"
img5 = Image.open(legend)
screen_image5 = ImageTk.PhotoImage(img5)
can.create_image((w / 3) + 260  ,((h / 2)+ (h / 3) + 40),
                                   anchor = NW, image = screen_image5)
print("Ready to connect...")

basename_1 = "image1.png"
basename_2 = "image2.png"
basename_3 = "image3.png"

serversocket.listen(1)                                           
while True:
    if(work == 'True'):
        # establish a connection
        clientsocket,addr = serversocket.accept()      
        print("Got a connection from %s" % str(addr))
        myfile1 = open(basename_1, "wb")
        while True:
            strng = clientsocket.recv(512)
            if not strng:
                break
            myfile1.write(strng)
        print("File 1")
        myfile1.close()
        
        clientsocket,addr = serversocket.accept()  
        myfile2 = open(basename_2, "wb")     
        while True:
            strng = clientsocket.recv(512)
            if not strng:
                break
            myfile2.write(strng)
        print("File 2")
        myfile2.close()

        clientsocket,addr = serversocket.accept()  
        myfile3 = open(basename_3, "wb")   
        while True:
            strng = clientsocket.recv(512)
            if not strng:
                 break
            myfile3.write(strng)
        print("File 3")
        myfile3.close()
        
        if(work == 'True'):
            screen1 = "image1.png"
            screen_image1 = ImageTk.PhotoImage(Image.open(screen1))
            can.create_image((w / 90) ,(h / 7),
                                   anchor = NW, image = screen_image1)
            screen2 = "image2.png"
            screen_image2 = ImageTk.PhotoImage(Image.open(screen2))
            can.create_image((w / 90) ,(h / 2),
                                   anchor = NW, image = screen_image2)
            screen3 = "image3.png"
            img = Image.open(screen3)
            #decrease of resolution
            img_resized = img.resize((1200,720))
            screen_image3 = ImageTk.PhotoImage(img_resized)
            can.create_image((w / 3) ,(h / 7),
                                   anchor = NW, image = screen_image3)
            root.update_idletasks()
            root.update()
        else:
            clientsocket.close()
            serversocket.close()
            break
    else:
        clientsocket.close()
        serversocket.close()
        break


