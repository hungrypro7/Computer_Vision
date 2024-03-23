import cv2 as cv

img1 = cv.imread('soccer.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('rose.png', cv.IMREAD_COLOR)
B, G, R = cv.split(img2)
img2 = R

if img1 is None or img2 is None:
    print("file not found")
    
ret1, thresh1 = cv.threshold(img1, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)       # 임계값, img
ret2, thresh2 = cv.threshold(img2, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)      # 임계값, img

font = cv.FONT_HERSHEY_SIMPLEX
position1 = (10, 900) 
position2 = (10, 30) 
cv.putText(thresh1, f'Otsu Threshold: {ret1}', position1, font, 1, (0,0,0), 2, cv.LINE_AA)
cv.putText(thresh2, f'Otsu Threshold: {ret2}', position2, font, 1, (255,255,255), 2, cv.LINE_AA)

print('Otsu Threshold', ret1)
print('Otsu Threshold', ret2)

titles = ['Original Image1', 'Original Image2', 'Otsu1','Otsu2']
images = [img1, img2, thresh1, thresh2]

for i in range(4):
    cv.imshow(titles[i], images[i])
    
cv.waitKey()
cv.destroyAllWindows()
