# Larry TO
# Created on: 12/12/2019
# Purpose: Simple tutorial to recognize sail number 

##==========Import Libraries
# Image processing libraries
import cv2
import numpy as np

# OCR libraries
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

##==========Process Image
fileName = "Images\Sail Number During Race\RUS-541.jpg"
img = cv2.imread(fileName)
imgBW = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)

# Setting any image value above 200 to be 255 and others to be zero 
_, threshold = cv2.threshold(imgBW, 170, 255, cv2.THRESH_BINARY)




# Finding contour 
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Show Image
# cv2.drawContours(threshold, contours, -1, (0, 255,0), 1)
# cv2.imshow("shapes", img)
# cv2.imshow("Threshold", threshold)
# cv2.waitKey(0)

# Sorting all the contours and selected area > 30 
contours = sorted(contours, key = cv2.contourArea, reverse = True) [:30]

# Show Image
# cv2.drawContours(threshold, contours, -1, (0, 255, 0), 1)
# cv2.imshow("shapes", img)
# cv2.imshow("Threshold", threshold)
# cv2.waitKey(0)

for cnt in contours:
	approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)

	if len(approx) == 4:
		sailNumCnt = approx

		x, y, w, h = cv2.boundingRect(cnt)
		new_img = img[y:y+h, x:x+w]
		cv2.imwrite('newimage.png', new_img)

		break


# cv2.drawContours(img, [sailNumCnt], -1, (255, 0, 0), -1)
# cv2.imshow("Threshold", img)
# cv2.waitKey(0)

##==========Extract Characters 
def ocr_core(imageValue):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(imageValue, lang='eng')  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core(new_img))


