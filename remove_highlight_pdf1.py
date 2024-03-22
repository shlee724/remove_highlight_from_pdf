import fitz  # PyMuPDF

def remove_highlight(input_pdf, output_pdf):
    # Open the PDF
    doc = fitz.open(input_pdf)

    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        
        # Get the annotations (highlights)
        annot = page.first_annot
        while annot:
            if annot.type[0] == 8:  # Check if annotation is a highlight
                page.delete_annot(annot)
            annot = annot.next

    # Save the modified PDF
    doc.save(output_pdf)
    doc.close()

# Usage
input_pdf = "test files/input.pdf"  # Input PDF file with highlights
output_pdf = "test files/output.pdf"  # Output PDF file with highlights removed

remove_highlight(input_pdf, output_pdf)