import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('checkerboardWithDots.png')
rows,cols,ch=img.shape

pts1=np.float32([[100,100],[300,100],[100,400]])   # 입력 이미지의 변환점
pts2=np.float32([[10,100],[200,50],[100,250]])     # 출력 이미지의 변환점

M = cv.getAffineTransform(pts1,pts2)    # 이동 변환에 사용할 변환 행렬 생성
dst=cv.warpAffine(img,M,(cols,rows))    # 이미지 변환

# 입력 이미지와 출력 이미지를 시각화함
plt.subplot(121),plt.imshow(img),plt.title('Input')  
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
