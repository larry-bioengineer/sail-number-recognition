# Larry TO
# Created on: 12/12/2019
# Purpose: Simple tutorial to recognize simple shapes 

# Import Libraries
import cv2
import numpy as np


img = cv2.imread("Images\Simple Shape\Group 1.png", cv2.IMREAD_GRAYSCALE)

# Setting any image value above 200 to be 255 and others to be zero 
_, threshold = cv2.threshold(img, 123, 255, cv2.THRESH_BINARY)

# Finding contour 
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for cnt in contours:
	cv2.drawContours(img, [cnt], -1, (0,255,0), 5)


# Approximation and draw contours on images 
# for cnt in contours:	

# 	approx = cv2.approxPolyDP(cnt, 0.05*cv2.arcLength(cnt, True), True) # True means the shape is enclosed, (col, row)
# 	cv2.drawContours(img, [approx], -1, (0,255,0), 5)
# 	# print(len(approx)) # number of corners 

# 	if len(approx) == 3:
# 		print(approx.ravel()) 


# Show Image
cv2.imshow("shapes", img)
cv2.imshow("Threshold", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()	