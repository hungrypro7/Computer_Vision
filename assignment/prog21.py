import cv2 as cv
import numpy as np

# 이미지 로드
original_image = cv.imread('tekapo.bmp')
original_image = cv.resize(original_image, (640, 320))
image = original_image.copy()

height, width = image.shape[:2]
center_coordinates = ((width-1) // 2, (height-1) // 2)
r, color, thickness = 5, (0, 0, 255), -1
cv.circle(image, center_coordinates, r, color, thickness)


def translate_image(img, dx, dy):
    translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
    return cv.warpAffine(img, translation_matrix, (width, height), borderMode=cv.BORDER_CONSTANT, borderValue=(0, 0, 0))

def rotate_image(img, angle):
    rotation_matrix = cv.getRotationMatrix2D(center_coordinates, angle, 1.0)
    rotated_image = cv.warpAffine(img, rotation_matrix, (width, height), borderMode=cv.BORDER_CONSTANT, borderValue=(0, 0, 0))
    return rotated_image

def scale_image(img, scale):
    scaled_width = int(width * scale)
    scaled_height = int(height * scale)
    scaled_img = cv.resize(img, (scaled_width, scaled_height), interpolation=cv.INTER_LINEAR)


    if scale > 1:  # 확대된 경우, 중앙 부분을 잘라냄
        start_x = (scaled_width - width) // 2
        start_y = (scaled_height - height) // 2
        cropped_img = scaled_img[start_y:start_y + height, start_x:start_x + width]
        return cropped_img
    
    else:  # 축소된 경우 또는 확대하지 않은 경우
        new_background = np.zeros((height, width, 3), np.uint8)
        top_left_x = (width - scaled_width) // 2
        top_left_y = (height - scaled_height) // 2
        new_background[top_left_y:top_left_y+scaled_height, top_left_x:top_left_x+scaled_width] = scaled_img
        return new_background

def mirror_image_y(img):
    mirrored_img = cv.flip(img, 1)
    return mirrored_img

def mirror_image_x(img):
    mirrored_img = cv.flip(img, 0)
    return mirrored_img

def transform_along_x_axis(img, pixels):
    new_width = width + pixels
    transformed_img = cv.resize(img, (new_width, height), interpolation=cv.INTER_LINEAR)
    if new_width > width:
        new_background = np.zeros((height, width, 3), np.uint8)
        start_x = (new_width - width) // 2
        new_background[:, :] = transformed_img[:, start_x:start_x+width]
        return new_background
    return transformed_img

def transform_along_y_axis(img, pixels):
    new_height = height + pixels
    transformed_img = cv.resize(img, (width, new_height), interpolation=cv.INTER_LINEAR)
    if new_height > height:
        new_background = np.zeros((height, width, 3), np.uint8)
        start_y = (new_height - height) // 2
        new_background[:, :] = transformed_img[start_y:start_y+height, :]
        return new_background
    return transformed_img

def apply_complex_transformation1(img):
    dx, dy = -5, -5  # 이동
    img_translated = translate_image(img, dx, dy)
    
    scale_factor = 0.5  # 축소
    img_scaled = scale_image(img_translated, scale_factor)
    
    angle = 10   # 반시계 방향 회전 
    img_rotated = rotate_image(img_scaled, angle)
    
    return img_rotated

def apply_complex_transformation2(img):
    dx, dy = 5, 5   # 이동
    img_translated = translate_image(img, dx, dy)

    scale_factor = 2  # 확대
    img_scaled = scale_image(img_translated, scale_factor)
    
    angle = -10  # 시계 방향 회전
    img_rotated = rotate_image(img_scaled, angle)
    
    return img_rotated


while True:
    cv.imshow('Image', image)

    key = cv.waitKey(0) & 0xFF

    if key == ord('T'):  # 'T' 눌렀을 때, 이미지를 상하좌우로 +-5픽셀씩 이동
        image = translate_image(image, 5, 5)
        
    elif key == ord('R'):  # 'R' 눌렀을 때, 반시계 방향으로 10도 회전
        image = rotate_image(image, 10)
    
    elif key == ord('S'):  # 'S' 눌렀을 때, 이미지를 0.5배로 축소
        image = scale_image(image, 0.5)
    
    elif key == ord('K'):  # 'K' 눌렀을 때, Y축 기준으로 이미지 미러링
        image = mirror_image_y(image)
        
    elif key == ord('L'):  # 'L' 눌렀을 때, X축 기준으로 이미지 미러링
        image = mirror_image_x(image)
    
    elif key == ord('I'):  # 'I' 눌렀을 때, 모든 변환 초기화 및 이미지 재설정
        image = original_image.copy()
        height, width = image.shape[:2]
        center_coordinates = ((width-1) // 2, (height-1) // 2)
        r, color, thickness = 5, (0, 0, 255), -1
        cv.circle(image, center_coordinates, r, color, thickness)
    
    elif key == ord('X'):  # 'X' 눌렀을 때, X축을 따라 이미지 변환 적용
        image = transform_along_x_axis(image, 50)
    
    elif key == ord('Y'):  # 'Y' 눌렀을 때, Y축을 따라 이미지 변환 적용
        image = transform_along_y_axis(image, 50)
    
    elif key == ord('1'):  # '1' 눌렀을 때, 복합 변환 1 적용
        image = apply_complex_transformation1(image)    
    
    elif key == ord('2'):  # '2' 눌렀을 때, 복합 변환 2 적용
        image = apply_complex_transformation2(image)
    
    elif key == 27:  # ESC 루프 탈출
        break

cv.destroyAllWindows()
