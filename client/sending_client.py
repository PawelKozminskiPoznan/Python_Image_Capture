import socket
from PIL import ImageGrab
import time

while(True):
    #crop((x1,y1,x2,y2))
    #(0,0)Start is on left, top corner
    #x1 and y1 are the left, top corner
    image_1 = ImageGrab.grab()
    image_1 = image_1.crop((5, 140, 590, 464))
    image_1.save('screenshot1.png')
    image_2 = ImageGrab.grab()
    image_2 = image_2.crop((5, 500, 590, 854))
    image_2.save('screenshot2.png')
    image_3 = ImageGrab.grab()
    image_3 = image_3.crop((700, 124, 1750, 902 ))
    image_3.save('screenshot3.png')
   

    image_1 = "screenshot1.png"
    image_2 = "screenshot2.png"
    image_3 = "screenshot3.png"
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    #host = '150.254.11.216'
    #host = '192.168.0.19'
    host = '192.168.0.6'
    port = 9999

    #connection to hostname on the port.
    s.connect((host, port))

    myfile1 = open(image_1, "rb")
    while True:
        strng = myfile1.readline(512)
        if not strng:
                break
        s.send(strng)
    myfile1.close()
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    myfile2 = open(image_2, "rb")
    while True:
        strng = myfile2.readline(512)
        if not strng:
                break
        s.send(strng)
    myfile2.close()
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    myfile3 = open(image_3, "rb")
    while True:
        strng = myfile3.readline(512)
        if not strng:
                break
        s.send(strng)
    myfile3.close()
    s.close()
    
    time.sleep(0.5)
