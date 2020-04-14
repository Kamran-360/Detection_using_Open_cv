import cv2
import numpy as np
cap=cv2.VideoCapture('k.avi')
_,frame1=cap.read()
_,frame2=cap.read()
while True:
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1,contours,-1,(0,244,0),2)
    for cont in contours:
        (x,y,w,h)=cv2.boundingRect(cont)
        if cv2.contourArea(cont) < 700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(124,233,44),2)
        print(frame1.shape)
        cv2.putText(frame1,"Status: {}".format('Movement'),(10,20),cv2.FONT_HERSHEY_COMPLEX,1,(0,200,0),2)
        cv2.putText(frame1,"Made by KAMI_360 Using Open-cv/python",(190,520),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)
        cv2.putText(frame1,"KAMI_360 Kindly Alert",(10,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,0),1)
    cv2.imshow('Detected',frame1)
    frame1=frame2
    ret,frame2=cap.read()
    if cv2.waitKey(5)==27:
        break
cap.release()
cv2.destroyAllWindows()