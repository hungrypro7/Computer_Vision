import cv2 as cv
import random

img = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print('File not found')
    
# add salt and pepper noise to img
noiseNum = img.size//10

for i in range(noiseNum):
    row = random.randrange(img.shape[0])
    col = random.randrange(img.shape[1])
    img[row,col] = (i % 2) * 255    

cv.imshow('Salt and pepper noise', img)    

# Apply Gaussian Filter
gaussian = cv.GaussianBlur(img, (3, 3), 0.0)
cv.imshow('Gaussian', gaussian)

# Apply Median Filter
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

cv.waitKey()
cv.destroyAllWindows()
