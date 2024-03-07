# 이 코드는 무한 루프를 돌면서 마우스 입력을 받아 사각형을 그림
import cv2 as cv
import sys

img = cv.imread('Erica.jpg')    # 'Erica.jpg'라는 이름의 이미지 파일을 읽어서 img 변수에 저장

if img is None:     # 이미지가 제대로 읽히지 않았을 때
    print('No file found')


# mouse callback function
def draw(event,x,y,flags,param):    
    if event == cv.EVENT_LBUTTONDOWN:   # 마우스 왼쪽 버튼을 누르면, 빨간색 사각형 그려짐
        cv.rectangle(img,(x,y),(x+100,y+100),(0,0,255),2)
    elif event == cv.EVENT_RBUTTONDOWN:     # 마우스 오른쪽 버튼을 누르면, 초록색 사각형 그려짐
        cv.rectangle(img,(x,y),(x+100,y+100),(0,255,0),2)
    cv.imshow('Drawing a rectangle', img)
    
cv.namedWindow('Drawing a rectangle')
cv.setMouseCallback('Drawing a rectangle',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        break
cv.destroyAllWindows()

