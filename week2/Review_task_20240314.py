import cv2 as cv
import numpy as np
import sys

img = cv.imread('Erica.jpg')
if img is None:
    print('File not found')
    sys.exit()

img = cv.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)

# 1 Change the hue by 180 degrees
h1 = (h + 90) % 180 
hue = cv.merge([h1, s, v])
hue = cv.cvtColor(hue, cv.COLOR_HSV2BGR)

# 2 Decrease the saturation by 50%
s1 = np.clip(s * 0.5, 0, 255).astype(hsv.dtype)
saturation = cv.merge([h, s1, v])
saturation = cv.cvtColor(saturation, cv.COLOR_HSV2BGR)

# 3 Increase the value by 50%
v1 = np.clip(v * 1.5, 0, 255).astype(hsv.dtype)
value = cv.merge([h, s, v1])
value = cv.cvtColor(value, cv.COLOR_HSV2BGR)

# Merge 2x2 images into a single image
top_row = np.hstack((img, hue))
bottom_row = np.hstack((saturation, value))
combined_image = np.vstack((top_row, bottom_row))

# Show the image
cv.imshow('Test', combined_image)
cv.imwrite('erica_new1.jpg', combined_image)

cv.waitKey(0)
cv.destroyAllWindows()