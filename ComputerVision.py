import cv2
import mediapipe as mp
import numpy as np

# image = np.ones((1000,1000,3)) # np.ones draws white background
# image = np.zeros((800,800,3))  # np.zeros draws black background

# image = np.ones((250,250,3))
# image[:] = 255,255,0 # B,G,R #Coloring with solid colors

# cv2.rectangle(image,(600,600),(100,100),(255,255,0),5)

image = cv2.imread('OTAKU.PNG')
# cv2.rectangle(image,(100,100),(200,200),(255,255,0),2)

# image = cv2.imread('OTAKU.PNG',0)  #Grayscale conversion with 0
# converted_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #Grayscale conversion

# ret, binary = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

# image_edited = cv2.resize(image,None,fx=0.5,fy=0.5) #Resizing the image. Scaling down
# image_edited = cv2.resize(image,None,fx=1.5,fy=1.5) #Resizing the image. Scaling up
# image_edited = cv2.resize(image,(1000,600)) # Custem scaling

cv2.imshow('Anime', image)
# cv2.imshow('Converted', converted_image)
# cv2.imshow('High contrast',binary)
# cv2.imshow('Image Resized', image_edited)

print(image.shape)
# print(converted_image.shape)
# print(binary.shape)
#
# v = cv2.VideoCapture(0)
#
#
#
# while True:
#     ret, frame = v.read()
#
#     canny = cv2.Canny(frame,20,25) #20,150
#     cv2.imshow('Live Cam', canny)
#
#     # cv2.imshow('Live Cam',frame)
#     if cv2.waitKey(1) == 13: # Until the Enter button is touched. 13->ENTER
#         break

cv2.waitKey(0)
# v.release()
cv2.destroyAllWindows()