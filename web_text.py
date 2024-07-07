import easyocr as ocr  
import streamlit as st  
from PIL import Image 
import numpy as np
import PyPDF2

st.title("Text from Images and PDFs")

st.markdown("## Extract Text From Image or PDF")

image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])
pdf = st.file_uploader(label="Upload your PDF here", type=['pdf'])

def load_model(): 
    reader = ocr.Reader(['en'], model_storage_directory='.', gpu=False)
    return reader 

reader = load_model() 

if image is not None:
    input_image = Image.open(image)
    st.image(input_image)
    with st.spinner("Processing image..."):
        result = reader.readtext(np.array(input_image))
        result_text = [text[1] for text in result]
        st.write(result_text)
else:
    st.write("Upload an image")


    

def extract_text_from_pdf(file):
    output_text = ""
    reader = PyPDF2.PdfReader(file)
    for i in range(len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        output_text += current_text
    return output_text


if pdf is not None:
    with st.spinner("Processing PDF..."):
        pdf_text = extract_text_from_pdf(pdf)
        st.write(pdf_text)
else:
    st.write("Upload a PDF")