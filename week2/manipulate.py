import cv2 as cv
import sys

img=cv.imread('Erica.jpg')

if img is None:
    print('File not found')

cv.imshow('Original', img)
# 이미지의 왼쪽 상단 1/4 부분을 추출하여 표시함
# 3차원 numpy 배열 형태로 img가 저장되며, 높이를 반으로 나누어 처음부터 중간까지의 범위를 선택
# 너비를 반으로 나누어 처음부터 중간까지의 범위를 선택, : 는 RGB 모두 선택
cv.imshow('Upperleft', img[0:img.shape[0]//2, 0:img.shape[1]//2, :])

# 이미지의 가운데 부분을 추출하여 표시함
# 3차원 numpy 배열 형태로 img가 저장되며, 높이의 1/4 지점에서 높이의 3/4 지점까지 범위를 선택
# 이미지 너비의 1/4 지점에서 시작하여 너비의 3/4 지점까지의 범위를 선택, : 는 RGB 모두 선택
cv.imshow('CenterHalf', img[img.shape[0]//4:3*img.shape[0]//4,
                            img.shape[1]//4:3*img.shape[1]//4, :])

# 빨간색 채널만을 추출하여 표시함
cv.imshow('R channel', img[:, :, 2])
# 초록색 채널만을 추출하여 표시함
cv.imshow('G channel', img[:, :, 1])
# 파란색 채널만을 추출하여 표시함
cv.imshow('B channel', img[:, :, 0])

cv.waitKey()
cv.destroyAllWindows()
