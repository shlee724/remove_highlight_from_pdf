#이건 이상하게도 망함... 일단은 쓰지 말것. chat gpt에서 가져온거임

import cv2

def remove_highlight(input_image_path, output_image_path):
    # Read the image
    image = cv2.imread(input_image_path)

    # Convert image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding to isolate highlighted areas (assuming highlighter is brighter than text)
    _, thresholded_image = cv2.threshold(grayscale_image, 200, 255, cv2.THRESH_BINARY_INV)

    # Invert the thresholded image
    inverted_thresholded_image = cv2.bitwise_not(thresholded_image)

    # Perform morphological operations to remove noise and smooth the image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    cleaned_image = cv2.morphologyEx(inverted_thresholded_image, cv2.MORPH_CLOSE, kernel)

    # Inpainting to fill in the highlighted areas
    result_image = cv2.inpaint(image, cleaned_image, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    # Show image
    cv2.imshow("test", result_image)
    cv2.waitKey(0)

    # Save the result
    cv2.imwrite(output_image_path, result_image)

# Usage
input_image_path = "test files/highlighted_text.jpg"  # Input image file with highlights
output_image_path = "test files/output_image.jpg"  # Output image file with highlights removed

remove_highlight(input_image_path, output_image_path)