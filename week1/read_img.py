import cv2 as cv
import sys

img = cv.imread('Erica.jpg')

if img is None:
    sys.exit('No file found')

cv.imshow('HY24011', img)

cv.waitKey()
cv.destroyAllWindows()
