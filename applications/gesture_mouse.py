
from ctypes import pythonapi
import time
import cv2
import mediapipe as mp
import pyautogui


print(pyautogui.size());

import sys

sys.path.insert(0, '../')
import HandTrackingModule as ht

detector=ht.handTracker()
cap=cv2.VideoCapture(0);
pTime=0;
cTime=0;


factorx=1920/640
factory=1080/480 

while True:
    success,img=cap.read();
    results=detector.get_results(img);
    #img=detector.draw_hands(img,results);
    
    img,coords=detector.draw_and_highlight_point(img,results,8)
    
    if coords!=[]:
        
        pyautogui.moveTo(1920-coords[0]*factorx, coords[1]*factory, duration = 0.001)
    
    
    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
    img=cv2.flip(img,1)
    cv2.imshow("Image",img)
    cv2.waitKey(1)