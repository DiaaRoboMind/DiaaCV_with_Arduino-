#from DiaaMind import python , CV 
import cv2
import mediapipe as mp
import math
import serial as se
import time 



mpH=mp.solutions.hands
hand=mpH.Hands()
mpDraw=mp.solutions.drawing_utils
ARD=se.Serial(port='/dev/ttyACM0',baudrate=9600,timeout=0.1)
Video=cv2.VideoCapture(0)

def send(lab,value):
    val=max(0,min(255,int(value*255)))
    ARD.write(lab.encode())
    ARD.write(bytes([val]))
    time.sleep(0.001)
while (True):
    Sc,img=Video.read()
    RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    get=hand.process(RGB)
    if (get.multi_hand_landmarks):
        for H in get.multi_hand_landmarks:
            base=H.landmark[4]
            # baseSe=H.landmark[4]
            F=H.landmark[8]
            S=H.landmark[12]
            T=H.landmark[16]
            Fu=H.landmark[20]
            d1=math.hypot(base.x-F.x,base.y-F.y)
            d2=math.hypot(base.x-S.x,base.y-S.y)
            d3=math.hypot(base.x-T.x,base.y-T.y)
            # d4=math.hypot(base.x-Fu.x,base.y-Fu.y)
            d5=math.hypot(base.x-Fu.x,base.y-Fu.y)
            if(d1<0.15):
                send('G',1-d1)
                
            else :
                send('G',0)
                
            if(d2<0.19):
                send ('Rs',1-d2)
            else :
                send('R',0)

            if(d3<0.23):
                send('B',1-d3)
            else :
                send('B',0)
            if(d5<0.15
               ):
                send('S',1-d5)
            # else :
            #   ARD.write(b'G')
            #   ARD.write(bytes([0]))
            #   ARD.write(b'R')
            #   ARD.write(bytes([0]))
            #   ARD.write(b'B')
            #   ARD.write(bytes([0]))
            #   ARD.write(b'S')
            #   ARD.write(bytes([0]))
            mpDraw.draw_landmarks(img,H,mpH.HAND_CONNECTIONS)
    cv2.imshow("Hand Led Sy by Diaa",img)
    if cv2.waitKey(1)&0xFF==ord('s'):
        break 


