import cv2 as cv

img=cv.imread('rose.png')
patch=img[250:350,170:270,:]    # 이미지 로드 및 특정 영역 선택

img=cv.rectangle(img,(170,250),(270,350),(255,0,0),3)    # 사각형 그리기/ 파란색 / 선의 두께 3
patch1=cv.resize(patch,dsize=(0,0),fx=5,fy=5,            # 가장 간단한 보간 방법 / 새로운 픽셀 값은 주변 픽셀 중에서 가장 가까운 픽셀의 값을 사용함
                 interpolation=cv.INTER_NEAREST)
patch2=cv.resize(patch,dsize=(0,0),fx=5,fy=5,            # 주변 4개 픽셀의 값을 사용하여 새로운 픽셀 값을 계산
                 interpolation=cv.INTER_LINEAR)
patch3=cv.resize(patch,dsize=(0,0),fx=5,fy=5,            #  주변 16개 픽셀의 값을 사용하여 새로운 픽셀 값을 계산
                 interpolation=cv.INTER_CUBIC)

cv.imshow('Original', img)
cv.imshow('Resize nearest', patch1)
cv.imshow('Resize bilinear', patch2)
cv.imshow('Resize bicubic', patch3)

cv.waitKey()
cv.destroyAllWindows()
