from PIL import Image
import pytesseract

# Load the image
image_path = '/mnt/data/image.png'
img = Image.open(image_path)

# Use Tesseract to extract text
extracted_text = pytesseract.image_to_string(img)

# Count the total number of words
word_count = len(extracted_text.split())
extracted_text, word_count
print(word_count)