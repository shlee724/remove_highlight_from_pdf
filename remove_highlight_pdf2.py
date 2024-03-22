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

        """
        # Save the image as JPG
        image_filename = f"{output_folder}/page_{page_num + 1}.jpg"
        pix._writeIMG(image_filename,"jpg", dpi)
        """
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
    channels = 3  # Assuming RGB format

    # Reshape the numpy array to the correct shape
    img_np = img_np.reshape((height, width, channels))

    # Convert from BGR to HSV
    img_hsv = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)

    # Extract the V channel
    out_img = img_hsv[:,:,2]

    return out_img

"""
def jpg_to_pdf(input_list, output_pdf):
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
"""


def images_to_pdf(image_list, output_pdf):
    # Create FPDF instance
    pdf = FPDF()

    # Add pages to the PDF using the images in the image list
    for image in image_list:
        pdf.add_page()
        pdf.image(image, x=0, y=0, w=210, h=297)  # Assuming A4 size (210x297 mm)

    # Save the PDF
    pdf.output(output_pdf)


# Usage
input_pdf = "test files/input.pdf"  # Input PDF file with highlights
output_pdf = "test files/output.pdf"  # Output PDF file with highlights removed
remove_highlight_pdf_main(input_pdf, output_pdf)