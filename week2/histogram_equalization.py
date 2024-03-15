# histogram equalization
import cv2 as cv
import matplotlib.pyplot as plt

gray=cv.imread('mistyroad.jpg', cv.IMREAD_GRAYSCALE)    # 이미지를 grayscale로 읽음
# or
# img=cv.imread('mistyroad.jpg') 
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)	

# 원본 그레이스케일 이미지를 화면에 표시, x축과 y축의 눈금을 제거
plt.imshow(gray,cmap='gray'), plt.xticks([]), plt.yticks([]), plt.show()    

# 히스토그램 계산
h=cv.calcHist([gray],[0],None,[256],[0,256])	
plt.plot(h,color='r',linewidth=1), plt.show()

# histogram equalization 수행
equal=cv.equalizeHist(gray)
plt.imshow(equal,cmap='gray'), plt.xticks([]), plt.yticks([]), plt.show()

# 빨간색 선으로 표시
h=cv.calcHist([equal],[0],None,[256],[0,256])	
plt.plot(h,color='r',linewidth=1), plt.show()
