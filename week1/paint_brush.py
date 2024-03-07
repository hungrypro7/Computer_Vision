import cv2 as cv
img = cv.imread('Erica.jpg')    

if img is None:
    print('No file found')
    
BrushSize=5     # 사용할 브러시의 크기 (5 pixel)
LColor,RColor=(255,0,0),(0,0,255)       # 왼쪽 클릭 시 Red, 오른쪽 클릭 시 Blue

def painting(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:     # 왼쪽 클릭 시
        cv.circle(img, (x,y), BrushSize, LColor, -1)
    elif event==cv.EVENT_RBUTTONDOWN:   # 오른쪽 클릭 시
        cv.circle(img, (x,y), BrushSize, RColor, -1)
    elif event==cv.EVENT_MOUSEMOVE:     # 마우스가 움직일 때, 마우스가 눌려져 있는 방향을 확인하여 해당하는 색상으로 원을 그림
        if flags==cv.EVENT_FLAG_LBUTTON:
            cv.circle(img, (x,y), BrushSize, LColor, -1)
        elif flags==cv.EVENT_FLAG_RBUTTON:
            cv.circle(img, (x,y), BrushSize, RColor, -1)
    cv.imshow('Painting', img)
    
cv.namedWindow('Painting')
cv.imshow('Painting', img)
cv.setMouseCallback('Painting', painting)

while(True):    # 무한 루프
    if cv.waitKey(1) == ord('q'):   # 'q'를 누르면 종료
        break
cv.destroyAllWindows()
