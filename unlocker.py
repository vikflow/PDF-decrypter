import pikepdf
import os

# Create temp directory if it doesn't exist
os.makedirs('temp', exist_ok=True)

pdf = pikepdf.open('865148076-KPSEA-MADE-FAMILIER-2022-2024.pdf', allow_overwriting_input=True)
pdf.save('temp/unlocked.pdf')