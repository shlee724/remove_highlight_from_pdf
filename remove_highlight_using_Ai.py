import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("fluo_pen_removal_model.h5")  # 모델 파일 경로

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (256, 256))  # 모델에 맞는 크기로 리사이즈
    image = image / 255.0  # 정규화
    return image


def remove_fluorescent_pen(image_path):
    image = preprocess_image(image_path)
    image = np.expand_dims(image, axis=0)  # 배치 차원 추가
    mask = model.predict(image)  # 형광펜을 감지하는 마스크 생성
    mask = (mask > 0.5).astype(np.uint8) * 255  # 이진화

    # 형광펜 영역 제거
    image = cv2.imread(image_path)
    image_no_pen = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    return image_no_pen

def save_image(image, output_path):
    cv2.imwrite(output_path, image)

def main():
    image_path = "input_image.jpg"  # 입력 이미지 
    output_path = "output_image.jpg"  # 출력 이미지 경로

    removed_image = remove_fluorescent_pen(image_path)
    save_image(removed_image, output_path)

if __name__ == "__main__":
    main()
