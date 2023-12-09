# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 23:44:33 2023

@author: Murat
"""

import cv2 as cv

#img = cv.imread("D:\ML Projects\Opencv_kursu\Resources\Photos\cat.jpg")
#cv.imshow("Cat", img)

#cv.waitKey(0)


capture=cv.VideoCapture("D:\ML Projects\Opencv_kursu\Resources\Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    
    cv.imshow("Video",frame)
    
    if cv.waitKey(20) & 0xFF==ord("d"):
        break
    
capture.release()
cv.destroyAllWindows()
