# image를 흑백으로 바꾸고, 크기를 조절할 수 있음
import cv2 as cv
import sys

img = cv.imread('Erica.jpg')

if img is None:
    sys.exit('No file found')

gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
gray_small = cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5)

cv.imwrite('Erica_gray.jpg', gray)
cv.imwrite('Erica_graysmall.jpg', gray_small)

cv.imshow('Color Image', img)
cv.imshow('Gray Image', gray)
cv.imshow('Gray Small Image', gray_small)

cv.waitKey()
cv.destroyAllWindows()
