from PIL import Image
from reportlab.pdfgen import canvas
import os

def create_pdf_from_images(folder_path, output_pdf_path):
    """
    Combines all PNG files from a folder into a single PDF file.

    Args:
        folder_path (str): The path to the folder containing the PNG files.
        output_pdf_path (str): The name and path for the output PDF file.
    """
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return

    # Get a list of all PNG files in the folder, sorted by name
    png_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])
    
    if not png_files:
        print(f"No PNG files found in the folder '{folder_path}'.")
        return

    # Create a PDF canvas object
    c = canvas.Canvas(output_pdf_path)

    for png_file in png_files:
        img_path = os.path.join(folder_path, png_file)
        
        try:
            # Open the PNG image and get its dimensions
            with Image.open(img_path) as img:
                width, height = img.size
                
                # Add a new page to the PDF with the same size as the image
                c.setPageSize((width, height))
                
                # Draw the image onto the PDF page
                c.drawImage(img_path, 0, 0, width, height)
                
                # Add the next page, unless this is the last image
                if png_file != png_files[-1]:
                    c.showPage()
                    
            print(f"Successfully added '{png_file}' to PDF.")
            
        except Exception as e:
            print(f"Failed to process file '{png_file}': {e}")
            
    # Save and close the PDF file
    c.save()
    print(f"\nSuccessfully created PDF: '{output_pdf_path}'")

# --- Script Usage ---
# Change the folder and output file names as needed
input_folder = "output"
output_file = "output_gabungan.pdf"

create_pdf_from_images(input_folder, output_file)