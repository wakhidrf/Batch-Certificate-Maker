import csv
from PIL import Image, ImageDraw, ImageFont
import os

# --- Configuration ---
INPUT_IMAGE_PATH = 'input/design.png'
FONT_PATH = 'font/font.ttf'
DATA_CSV_PATH = 'data.csv'
OUTPUT_FOLDER = 'output'

# Coordinates and size
NIM_POSITION = (710, 635)
NAMA_POSITION = (710, 555)

# Separate font sizes for NIM and Nama
NIM_FONT_SIZE = 64
NAMA_FONT_SIZE = 72

# --- Main function to create certificates ---
def create_certificate(nim, nama):
    try:
        # Open the certificate design image
        img = Image.open(INPUT_IMAGE_PATH)
        draw = ImageDraw.Draw(img)

        # Load fonts from file with different sizes
        nim_font = ImageFont.truetype(FONT_PATH, NIM_FONT_SIZE)
        nama_font = ImageFont.truetype(FONT_PATH, NAMA_FONT_SIZE)

        # Function to write text centered on the X-axis
        def draw_centered_text(text, position, font, draw_obj):
            # Get text bounding box
            text_bbox = draw_obj.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            
            # Calculate new X position to center the text
            x_centered = position[0] - (text_width / 2)
            
            # Write text on the image
            draw_obj.text((x_centered, position[1]), text, font=font, fill=(0, 0, 0))

        # Write NIM
        draw_centered_text(nim, NIM_POSITION, nim_font, draw)
        
        # Write Name
        draw_centered_text(nama, NAMA_POSITION, nama_font, draw)

        # Save the certificate to the output folder in PNG format
        output_png_path = f"{OUTPUT_FOLDER}/sertifikat_{nim}.png"
        img.save(output_png_path)
        
        print(f"✅ Certificate for {nama} ({nim}) successfully created.")

    except Exception as e:
        print(f"❌ Failed to create certificate for {nama} ({nim}). Error: {e}")

# --- Main program ---
if __name__ == "__main__":
    # Create the output folder if it doesn't exist
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Read data from the CSV file
    try:
        with open(DATA_CSV_PATH, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                nim = row['nim']
                nama = row['nama']
                create_certificate(nim, nama)
        print("\nProcess finished. Check your 'output' folder.")

    except FileNotFoundError:
        print(f"❌ Error: File '{DATA_CSV_PATH}' not found.")
    except KeyError:
        print(f"❌ Error: 'nim' or 'nama' column not found in the CSV file.")