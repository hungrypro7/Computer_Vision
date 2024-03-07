# 화면에 도형과 글자를 띄울 수 있음
import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)     # 512x512 픽셀 크기에 색상 채널이 3개(RGB)인 검은색의 빈 이미지를 생성 / 데이터 타입 : uint8
cv.line(img, (0, 0), (255, 255), (0, 0, 255), 5)    # 위치 : (0, 0) ~ (255, 255) / 이미지에 파란색(BGR 색상에서 파란색은 (0, 0, 255))의 두께가 5인 선을 그림
cv.rectangle(img, (200, 150), (300, 360), (0, 255, 0), 3)   # 위치 : LP(200, 150) ~ RD(300, 360) / 이미지에 초록색의 두께가 3인 사각형을 그림
cv.circle(img, (450, 50), 50, (255, 0, 0), -1)      # 위치 : center(450, 50), 반지름이 50인 원, Red, 색상 채우기 -1
cv.ellipse(img, (400, 250), (100, 50), 0, 0, 180, 255, -1)      # 위치 : center(400, 250), (가로축, 세로축) 타원, 0~180도, 테두리 색상 255, 색상 채우기 -1

cv.putText(img, 'HY24011', (10, 500), cv.FONT_HERSHEY_SIMPLEX,
2, (255, 255, 255), 2)      # 'HY24011'이라는 텍스트를 이미지 (10, 500) 위치에 추가, cv.FONT_HERSHEY_SIMPLEX 폰트, 폰트 크기 2, 두께 2

cv.imshow('Drawing Features', img)

cv.waitKey()
cv.destroyAllWindows()
