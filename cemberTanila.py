import math
import cv2
import numpy as np
from gucVer import *
from ilerle import *

def cemberTanila():
    cap = cv2.VideoCapture(0)
    value = True
    returnValue = False
    waitingCount = 0

    while (value):  
        ret, frame = cap.read()
        windowWidth=frame.shape[1]
        windowHeight=frame.shape[0]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frameBlur = cv2.blur(frame, (5, 5))
        edge = cv2.Canny(frameBlur, 50, 120)
        edgeDilate = cv2.dilate(edge, cv2.getStructuringElement(cv2.MORPH_RECT,(2,2)))   
        frameCopy = cv2.cvtColor(frameBlur, cv2.COLOR_GRAY2BGR) 
        circles = cv2.HoughCircles(edgeDilate,cv2.HOUGH_GRADIENT, 1, 20, param1=50,param2=75,minRadius=25,maxRadius=0)
        
        if circles is not None:
            waitingCount = 0
            circles = np.uint16(np.around(circles))
            for c in circles[0]:
            #while (True):
                #cv2.circle(frameCopy,(c[0],c[1]),c[2],(0,255,0),2)
                #print("x: ", c[0], "y: ", c[1])
                if(c[0] - (windowWidth/2) > 0):
                    gucVer(0, 1, 0, 0) #saga dönüs yap
                if(c[0] - (windowWidth/2) < 0):
                    gucVer(1, 0, 0, 0) #sola dönüs yap
                if(c[1] - (windowHeight/2) > 0):
                    gucVer(0, 0, 1, 0) #asagi yönel
                if(c[1] - (windowHeight/2) < 0):
                    gucVer(0, 0, 0, 1) #yukari yönel
                if(c[2] < windowHeight or c[2] < windowWidth):
                    ilerle() #cemberden gecene kadar ileri güc ver
                if(c[2] > windowHeight/2 or c[2] > windowWidth/2):
                    for i in range(100):
                        ilerle() #cember ortalandi ve gecmek icin tam ileri
                    returnValue = True
                    value = False #cemberden gecildi donguden cik
        else:
            waitingCount = waitingCount + 1
            print("Bekleniyor... ", waitingCount)
            if(waitingCount == 200):
                value = False
                returnValue = False #cember bulunamadi
        
        #cv2.imshow("frame", frameCopy)
    
    cap.release()
    cv2.destroyAllWindows()
    return returnValue