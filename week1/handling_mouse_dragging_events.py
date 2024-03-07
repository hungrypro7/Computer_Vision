# 이 코드는 마우스를 드래그해서 이미지 위에서 사각형을 그릴 수 있음
import cv2 as cv
import sys

img = cv.imread('Erica.jpg')

if img is None:
    print('No file found')


# mouse callback function
def draw(event,x,y,flags,param):
    global ix, iy;
    
    if event == cv.EVENT_LBUTTONDOWN:   # 마우스를 손으로 누를 때
        ix,iy=x,y
    elif event == cv.EVENT_LBUTTONUP:   # 마우스를 손에서 뗄 때
        cv.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
    cv.imshow('Drawing a rectangle', img)
    
cv.namedWindow('Drawing a rectangle')
cv.setMouseCallback('Drawing a rectangle',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        break
cv.destroyAllWindows()

