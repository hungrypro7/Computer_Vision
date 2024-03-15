import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('Erica.jpg') 
h=cv.calcHist([img],[2],None,[256],[0,256])     # 히스토그램 계산 (픽셀 값 범위 : [0, 256])
plt.plot(h,color='r',linewidth=1)       # 계산된 히스토그램을 빨간색 선으로 표시
