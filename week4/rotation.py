import cv2 as cv

img=cv.imread('tekapo.bmp')
rows, cols,channels = img.shape

M=cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 
                         30, 1)    # 회전 중심점((cols-1)/2.0, (rows-1)/2.0), 회전 각도(30), 및 스케일(1)을 인자로 받아 회전 변환 행렬을 생성
dst = cv.warpAffine(img, M, (cols, rows))    # 이미지 회전 변환함

cv.imshow('Original', img)
cv.imshow('Rotation', dst)

cv.waitKey()
cv.destroyAllWindows()
