# Gamma correction
import cv2 as cv
import numpy as np

img=cv.imread('erica.jpg') 
img=cv.resize(img,dsize=(0,0),fx=0.25,fy=0.25)      # 이미지의 크기를 원본의 25%로 조정함


def gamma(f,gamma=1.0):
    fi = f/255.0
    f = np.uint8(255*(fi**gamma))
    return f

gc=np.hstack((gamma(img,0.5),gamma(img,0.75),gamma(img,1.0),
              gamma(img,2.0),gamma(img,3.0)))        # 이미지들을 가로로 연결하여 하나의 이미지를 만듬
cv.imshow('gamma',gc)       # 가로로 연결된 이미지를 gamma 창에 표시

cv.waitKey()
cv.destroyAllWindows()
