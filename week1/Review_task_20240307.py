import cv2 as cv
import sys

img = cv.imread('Erica.jpg')

if img is None:
    sys.exit('No file found')

temp = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
gray = cv.cvtColor(temp, cv.COLOR_GRAY2BGR)

cv.rectangle(gray, (120, 320), (790, 520), (255, 0, 255), 3)
cv.putText(gray, '2019098068', (10, 560), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv.imshow('Gray Image', gray)
cv.imwrite('Gray_image.jpg', gray)

cv.waitKey()
cv.destroyAllWindows()