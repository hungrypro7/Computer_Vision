import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('sudoku.jpg')
rows,cols,ch=img.shape

pts1=np.float32([[75,86],[490,71],[36,513],[517,520]])    # 입력 이미지의 4개 변환점
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])      # 출력 이미지의 4개 변환점

M = cv.getPerspectiveTransform(pts1,pts2)       # 원근 변환 행렬 생성
dst = cv.warpPerspective(img,M,(300,300))       # 이미지를 원근 변환함 (300, 300)은 이미지 크기

upts1 = np.uint16(pts1)
for i in range(4):    # 입력 이미지에 변환점 표시
    cv.circle(img,(upts1[i,0],upts1[i,1]),8,(0,255,0),-1)

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
