import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('JohnHancocksSignature.png',cv.IMREAD_UNCHANGED) 
t,bin_img=cv.threshold(img[:,:,3],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
plt.imshow(bin_img,cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

b=bin_img[235:420, 770:1040]
plt.imshow(b, cmap='gray'), plt.xticks([]), plt.yticks([])   # 원본 이미지
plt.show()

# structuring element 구조 요소
se=np.uint8([[0,0,1,0,0],
             [0,1,1,1,0],
             [1,1,1,1,1],
             [0,1,1,1,0],
             [0,0,1,0,0]])

# dilation operation
b_dilation=cv.dilate(b, se, iterations=1)
plt.imshow(b_dilation, cmap='gray'), plt.xticks([]), plt.yticks([])    # 팽창 / 흰색 이미지 영역을 확장시킴, 빈 구멍들이 채워짐
plt.show()

# erosion operation
b_erosion=cv.erode(b, se, iterations=1)    # 침식 / 흰색 영역을 축소시킴, 객체의 크기가 줄어들고 작은 객체가 사라질 수 있음
plt.imshow(b_erosion, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

# Write closing and opening operations 팽창 -> 침식 적용
b_closing=cv.erode(cv.dilate(b, se, iterations=1), se, iterations=1)    # 닫기 / 객체의 모양을 보존하면서 노이즈 제거에 효과적임
plt.imshow(b_closing, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

# 침식 -> 팽창 적용
b_opening=cv.dilate(cv.erode(b, se, iterations=1), se, iterations=1)    # 열기 / 작은 객체나 노이즈를 제거하는데 사용됨, 객체의 모서리를 부드럽게 만들어줌
plt.imshow(b_opening, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()
