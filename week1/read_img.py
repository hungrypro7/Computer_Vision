# 같은 폴더 내에 jpg 파일을 위치시킬 것!
# 이미지를 읽어와서 화면에 띄움
import cv2 as cv
import sys

img = cv.imread('Erica.jpg')

if img is None:
    sys.exit('No file found')

cv.imshow('HY24011', img)

cv.waitKey()
cv.destroyAllWindows()
