import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#img = cv.imread('Photos/cat.jpg')
#cv.imshow('Cat',img)

#blank[200:300,300:400] = 0,255,0
#cv.imshow('Green',blank)

cv.rectangle(blank,(0,0),(250,500),(255,0,0),thickness=2)
cv.imshow('rectangle',blank)

cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
cv.imshow('circle',blank)

cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
cv.imshow('line',blank)

cv.waitKey(0)
