import fitz  # PyMuPDF

def pdf_to_high_quality_images(input_pdf, output_folder, dpi=300):
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

        # Save the image as PNG
        image_filename = f"{output_folder}/page_{page_num + 1}.png"
        pix._writeIMG(image_filename,"jpg", dpi)

    # Close the PDF
    doc.close()

# Usage
input_pdf = "test files/input.pdf"  # Input PDF file
output_folder = "test files/output_images"  # Output folder for images
dpi = 300  # DPI for high resolution images (default: 300)

pdf_to_high_quality_images(input_pdf, output_folder, dpi)

