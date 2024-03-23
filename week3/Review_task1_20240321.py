import cv2 as cv
import numpy as np

img = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("file not found")

bImg = cv.blur(img, (5,5))    

sumimg = cv.integral(img)
bImg2 = np.zeros((img.shape[0], img.shape[1]))      # 그림 크기의 모든 칸이 0인 격자 생성

# write filtering with a 5x5 using sumimg
kernel_size = 5
half = kernel_size // 2
for y in range(half, img.shape[0] - half):
    for x in range(half, img.shape[1] - half):
        total = sumimg[y + half + 1, x + half + 1] - sumimg[y + half + 1, x - half] - sumimg[y - half, x + half + 1] + sumimg[y - half, x - half]
        bImg2[y, x] = total / (kernel_size ** 2)

bImg2 = np.uint8(np.clip(bImg2, 0, 255))

titles = ['Original Image','Blurred', 'With IntegralImg']
images = [img, bImg, bImg2]

for i in range(3):
    cv.imshow(titles[i], images[i])
cv.waitKey()
cv.destroyAllWindows()
