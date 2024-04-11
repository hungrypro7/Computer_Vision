import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 이미지 로드
image = cv.imread('foldingScreen8.jpg')
cv.imshow('input', image)

height, width = image.shape[:2]
center_x, center_y = width / 2, height / 2

# 이미지 스케일 조정
transformation_matrix = cv.getRotationMatrix2D((center_x, center_y), 0, 0.5)
resized_image = cv.warpAffine(image, transformation_matrix, (width, height))

affine = 50 * (3 ** (-1/2))

transformed_image1 = np.zeros_like(resized_image)
transformed_image2 = np.zeros_like(resized_image)

cv.imshow('resized', resized_image)

# 분할된 각 부분에 아핀 변환 적용
for i in range(8):
    
    if i % 2 == 0:
        # 각 사각형 부분의 원본 좌표 (상단 왼쪽, 상단 오른쪽, 하단 왼쪽)
        pts1 = np.float32([
            [200 + (50 * i), 95], 
            [200 + 50 * (i + 1), 95], 
            [200 + 50 * (i + 1), 270]
        ])
        
        pts2 = np.float32([
            [200 + (50 * i), 95], 
            [200 + 50 * (i + 1), 95 - affine],  
            [200 + 50 * (i + 1), 270 - affine]
            ])

    else:
        # 각 사각형 부분의 원본 좌표 (상단 왼쪽, 상단 오른쪽, 하단 왼쪽)
        pts1 = np.float32([
            [200 + (50 * i), 95], 
            [200 + (50 * i), 270], 
            [200 + 50 * (i + 1), 270]
        ])
        
        pts2 = np.float32([
            [200 + (50 * i), 95 - affine], 
            [200 + (50 * i), 270 - affine],
            [200 + 50 * (i + 1), 270]  
            ])
    
    # 아핀 변환 행렬 계산
    M = cv.getAffineTransform(pts1, pts2)
    
    # 아핀 변환 적용
    part_transformed = cv.warpAffine(resized_image, M, (width, height))
    
    # 변환된 부분만 결과 이미지에 복사
    transformed_image1[60:280, 200+(50*i):200+50*(i+1)] = part_transformed[60:280, 200+(50*i):200+50*(i+1)]

# 결과 이미지 표시
cv.imshow('Affine_Transformed', transformed_image1)
cv.imwrite('./folding_affine.jpg', transformed_image1)

for i in range(8):
    
    if i % 2 == 0:
        # 각 사각형 부분의 원본 좌표 (상단 왼쪽, 상단 오른쪽, 하단 왼쪽)
        pts1 = np.float32([
            [200 + (50 * i), 95], 
            [200 + 50 * (i + 1), 95],
            [200 + (50 * i), 270],
            [200 + 50 * (i + 1), 270]
        ])
        
        pts2 = np.float32([
            [200 + (50 * i), 95], 
            [200 + 50 * (i + 1), 95 + affine],
            [200 + (50 * i), 270],
            [200 + 50 * (i + 1), 270 - affine]
        ])

    else:
        # 각 사각형 부분의 원본 좌표 (상단 왼쪽, 상단 오른쪽, 하단 왼쪽)
        pts1 = np.float32([
            [200 + (50 * i), 95], 
            [200 + 50 * (i + 1), 95],
            [200 + (50 * i), 270],
            [200 + 50 * (i + 1), 270]
        ])
        
        pts2 = np.float32([
            [200 + (50 * i), 95 + affine], 
            [200 + 50 * (i + 1), 95],
            [200 + (50 * i), 270 - affine],
            [200 + 50 * (i + 1), 270] 
        ])
    
    # Perspective 변환 행렬 계산
    M = cv.getPerspectiveTransform(pts1, pts2)
    
    # Perspective 변환 적용
    part_transformed = cv.warpPerspective(resized_image, M, (width, height))
    
    # 변환된 부분만 결과 이미지에 복사
    transformed_image2[60:280, 200+(50*i):200+50*(i+1)] = part_transformed[60:280, 200+(50*i):200+50*(i+1)]

# 결과 이미지 표시
cv.imshow('Perspective_Transformed', transformed_image2)
cv.imwrite('./folding_perspective.jpg', transformed_image2)

cv.waitKey()
cv.destroyAllWindows()
