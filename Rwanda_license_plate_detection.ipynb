import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('rada.jpg')
plt.imshow(img)

""" Create a function that displays the image in a
 larger scale and correct coloring for matplotlib.
 """
 
 def display(img):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ax.imshow(new_img)
    
display(img)

"""
 Load the haarcascade_russian_plate_number.xml file.

""""

plate_cascade = cv2.CascadeClassifier('../DATA/haarcascades/haarcascade_russian_plate_number.xml')

"""
Create a function that takes in an image and draws a rectangle around 
what it detects to be a license plate. Keep in mind we're just drawing a
 rectangle around it for now, later on we'll adjust this function to blur.
"""
def detect_plate(img):
    
  
    plate_img = img.copy()
  
    plate_rects = plate_cascade.detectMultiScale(plate_img,scaleFactor=1.3, minNeighbors=3) 
    
    for (x,y,w,h) in plate_rects: 
        cv2.rectangle(plate_img, (x,y), (x+w,y+h), (0,0,255), 4) 
        plate_img = img.copy()
        roi = img.copy()
        roi = roi[y:y+h,x:x+w]
        
        
    return roi

result = detect_plate(img)
display(result)

