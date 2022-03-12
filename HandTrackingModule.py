from selectors import DefaultSelector
import time
import cv2
import mediapipe as mp


class handTracker():
    def __init__(self,mode_static=False,num_hands=2):
        self.mode_static=mode_static;
        self.num_hands=num_hands;
        #########
        self.mpHand=mp.solutions.hands
        self.hands=self.mpHand.Hands(self.mode_static,self.num_hands)
        self.mpDraw=mp.solutions.drawing_utils
        #########
    
    def get_results(self,img):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results=self.hands.process(imgRGB)
        
        return results

    def draw_hands(self,img,results,draw=False):
        
        #print(results)
        
        
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:

                self.mpDraw.draw_landmarks(img,handLms,self.mpHand.HAND_CONNECTIONS)
        #return img and results
        return img
    

    def draw_and_highlight_point(self,img,results,point_no):
        coords=[]
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                lm=handLms.landmark[point_no]
                h,w,c=img.shape
                #print(h,w);
                cx,cy=int(lm.x*w),int(lm.y*h);
                coords=[cx,cy]
                cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED);
        return img,coords;
def main():
    detector=handTracker();
    cap=cv2.VideoCapture(0);
    pTime=0;
    cTime=0;

    while True:
        success,img=cap.read();
        results=detector.get_results(img)
        img=detector.draw_hands(img,results);
        
        img,coords=detector.draw_and_highlight_point(img,results,8)
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(10,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
        
        

        cv2.imshow("Image",img)
        cv2.waitKey(1)
        
if __name__=="__main__":
    main()