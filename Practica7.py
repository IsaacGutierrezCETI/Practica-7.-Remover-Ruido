#Isaac Alejandro Gutiérrez Huerta 19110198 7E1
#Sistemas de Visión Artificial

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#Hue Saturation Value

    #ROJO
    lower_color1 = np.array([0,150,180])
    upper_color1 = np.array([15,255,255])

    #AZUL
    lower_color2 = np.array([100,90,130])
    upper_color2 = np.array([150,255,255])

    #VERDE
    lower_color3 = np.array([40,50,150])
    upper_color3 = np.array([80,255,255])
    
    mask = cv2.inRange(hsv, lower_color1, upper_color1)
    mask_orig=mask
    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((5,5),np.uint8)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    #mask = opening
    #opening_color = cv2.bitwise_and(frame, frame, mask = mask)
    
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    #mask = closing
    #closing_color = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask_orig)
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)
    
    if cv2.waitKey(1) & 0xFF == ord('i'):
        break

cap.release()
cv2.destroyAllWindows()
