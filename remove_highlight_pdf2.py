#used remove_highlight_jpg1.py's algorithm
import cv2
import numpy as np
import fitz  # PyMuPDF
from fpdf import FPDF
import os

def pdf_to_high_quality_jpg(input_pdf, output_folder, dpi=300):
    # Open the PDF
    doc = fitz.open(input_pdf)

    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)

        # Determine the size of the output image based on DPI
        zoom_x = dpi / 72.0
        zoom_y = dpi / 72.0
        mat = fitz.Matrix(zoom_x, zoom_y)

        # Render the page as an image
        pix = page.get_pixmap(matrix=mat)

        # Save the image as JPG
        image_filename = f"{output_folder}/page_{page_num + 1}.jpg"
        pix._writeIMG(image_filename,"jpg", dpi)

    # Close the PDF
    doc.close()


def remove_highlight(img):
    # Convert from BGR to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Extract the V channel
    out_img = img_hsv[:,:,2]
    # Display the image
    cv2.imshow('output_image', out_img)
    cv2.waitKey(0)
    cv2.imwrite('output.jpg', out_img)


def jpg_to_pdf(input_folder, output_pdf):
    # Create FPDF instance
    pdf = FPDF()

    # Iterate through each file in the input folder
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".png"):
            try:
                # Add a page to the PDF
                pdf.add_page()

                # Set image format and add image to PDF
                pdf.image(os.path.join(input_folder, filename), x=0, y=0, w=210, h=297)  # Assuming A4 size (210x297 mm)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                continue

    # Save the PDF
    pdf.output(output_pdf)

