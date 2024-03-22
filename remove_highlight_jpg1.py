#일단은 이게 젤 깔끔한데..?
import cv2

def remove_highlight(img):
    # Convert from BGR to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Extract the V channel
    out_img = img_hsv[:,:,2]
    # Display the image
    cv2.imshow('output_image', out_img)
    cv2.waitKey(0)
    cv2.imwrite('output.jpg', out_img)

# read the image
img = cv2.imread('C:/dev/python test/test files/output_images/page_1.jpg')
remove_highlight(img)