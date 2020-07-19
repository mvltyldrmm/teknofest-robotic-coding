import cv2
import numpy as np
x,y,radius  = 0,0,0
colorLower = (24, 100, 100) 
colorUpper = (44, 255, 255)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv,colorLower,colorUpper)  #sari maskelendi

    mask = cv2.erode(mask,None,iterations=2)
    mask = cv2.dilate(mask,None,iterations=2)

    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) >0 :
        c = max(cnts, key=cv2.contourArea)
        ((x,y),radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)

        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
            cv2.circle(frame,center,5,(0,0,255),-1)
            print("BUYUK CİSİM DENİZALTI OLABİLİR")


    cv2.imshow("frame",mask)
    cv2.waitKey(20)

    print("x : ")
    print(x)
    print("y : ")
    print(y)
    print("büyüklük : ")
    print(radius)


cap.release()
cv2.destroyAllWindows()