import cv2
import numpy as np

img = cv2.imread('test files/output_images/page_1.jpg')

def remove_highlight(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gaus = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 8)
    image, otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    #대충 테스트 결과 - otsu가 훨씬 화질이 좋다

    cv2.imshow("Gaussian", gaus)
    cv2.imshow("Otsu", otsu)
    cv2.waitKey(0)

    cv2.imwrite('output.png', gaus)

remove_highlight(img)
