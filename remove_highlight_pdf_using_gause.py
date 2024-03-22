#used remove_highlight_jpg1.py's algorithm
import cv2
import numpy as np
import fitz  # PyMuPDF
from fpdf import FPDF
import os

def remove_highlight_pdf_main(input_pdf, output_file_path):
    jpg_list = pdf_to_high_quality_jpg(input_pdf)

    i = 0
    for image in jpg_list:
        jpg_list[i] = remove_highlight(image)
        i += 1
    
    images_to_pdf(jpg_list,output_file_path)


def pdf_to_high_quality_jpg(input_pdf, dpi=300):
    # Open the PDF
    doc = fitz.open(input_pdf)
    image_list = []

    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)

        # Determine the size of the output image based on DPI
        zoom_x = dpi / 72.0
        zoom_y = dpi / 72.0
        mat = fitz.Matrix(zoom_x, zoom_y)

        # Render the page as an image
        pix = page.get_pixmap(matrix=mat)

        image_list.append(pix)

    # Close the PDF
    doc.close()
    return image_list


def remove_highlight(img):
    # Convert pixmap to numpy array
    img_np = np.frombuffer(img.samples, dtype=np.uint8)

    # Determine the shape of the image
    height = img.height
    width = img.width
    channels = 3  # Assuming RGBA format

    # Reshape the numpy array to the correct shape
    img_np = img_np.reshape((height, width, channels))

    # Convert from RGBA to grayscale
    img_gray = cv2.cvtColor(img_np, cv2.COLOR_RGBA2GRAY)

    # Apply adaptive thresholding
    _, gaus = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    __, otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return otsu




def images_to_pdf(image_list, output_pdf):
    # Create FPDF instance
    pdf = FPDF()

    # Add pages to the PDF using the images in the image list
    for i, image in enumerate(image_list):
        # Save the image to a temporary file
        image_path = f"temp_image_{i}.png"
        cv2.imwrite(image_path, image)

        # Add the image to the PDF
        pdf.add_page()
        pdf.image(image_path, x=0, y=0, w=210, h=297)  # Assuming A4 size (210x297 mm)

        # Remove the temporary image file
        os.remove(image_path)

    # Save the PDF
    pdf.output(output_pdf)


# Usage
input_pdf = "test files/input.pdf"  # Input PDF file with highlights
output_pdf = "test files/output.pdf"  # Output PDF file with highlights removed
remove_highlight_pdf_main(input_pdf, output_pdf)