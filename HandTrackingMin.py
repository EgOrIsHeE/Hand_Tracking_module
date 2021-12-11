import cv2 as cv
import mediapipe as mp
import time
import numpy as np

cap = cv.VideoCapture(0)  # getting webcam picture
succes, img = cap.read()
h, w, ch = tuple(img.shape) #getting webcam res



mpHands = mp.solutions.hands #creates hands object using code from mp for actual detection
hands = mpHands.Hands() #using default params
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:  # going in loop in video
    succes, img = cap.read()  # getting frame to img
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB) #by defauly in BGR, and mpHands works with RGB
    results = hands.process(imgRGB) #cords of hand(s) if there are some, else None

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(hand.landmark):
                cx, cy = (int(lm.x * w), int(lm.y*h)) #getting cords in pixels






    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (30, 50),cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3 )

    cv.imshow('Image', img)  # showing img
    if cv.waitKey(1) & 0xFF == ord('q'):  # if you press q you close the video window
        break

