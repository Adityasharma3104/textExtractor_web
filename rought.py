import pytesseract as tess
from PIL import Image

img = Image.open('model\\test_img.jpg')
text = tess.image_to_string(img)
print(text)



