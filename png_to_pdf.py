from fpdf import FPDF
import os

def png_to_pdf(input_folder, output_pdf):
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

input_folder="test files/output_images"
output_pdf = "test files/output_pdf.pdf"

png_to_pdf(input_folder, output_pdf)