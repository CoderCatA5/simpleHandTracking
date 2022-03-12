import time

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHand=mp.solutions.hands

#static image_mode false
#second parameter for no of hands
hands=mpHand.Hands(False,4)
mpDraw=mp.solutions.drawing_utils


#for fps
pTime=0
cTime=0

while True:
    success,img=cap.read()
    
    #simple converts color 
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results=hands.process(imgRGB)
    print(results)


    #results.multi_hand_landmarks     shows hand landmarkers 21 of them to track hand locations
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm)
                # gives x y z values of markers in terms of percentage
                h,w,c=img.shape
    conda install -c conda-forge pyautogui
                cx,cy=int(lm.x*w),int(lm.y*h);
                
                print(id,cx,cy)
                if id==4:
                    cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED);
            
            #draw landmarks over images 
            #mpDraw.draw_landmarks(img,handLms)
            mpDraw.draw_landmarks(img,handLms,mpHand.HAND_CONNECTIONS)
    
    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
    
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)
