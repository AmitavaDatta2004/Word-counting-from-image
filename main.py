from PIL import Image
import pytesseract

# Load the image
image_path = 'image.png'  # Replace with the path to your image
img = Image.open(image_path)

# Use Tesseract to extract text from the image
extracted_text = pytesseract.image_to_string(img)

# Count the total number of words
word_count = len(extracted_text.split())

# Print the extracted text and word count
print("Extracted Text:\n", extracted_text)
print("\nTotal Word Count:", word_count)