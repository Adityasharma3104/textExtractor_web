# textExtractor_web
an web streamlit GUI that extracts text from images and pdf .


Here's a README file for your Streamlit application that extracts text from images and PDFs:

---

This Streamlit application allows users to extract text from uploaded images and PDF files using EasyOCR and PyPDF2 libraries.

## Features

- Extract text from image files (.png, .jpg, .jpeg) using EasyOCR.
- Extract text from PDF files (.pdf) using PyPDF2.
- Display the extracted text directly in the web application.

## Requirements

- Python 3.x
- Streamlit
- EasyOCR
- PyPDF2
- PIL (Pillow)
- NumPy

## Installation

1. Clone the repository or download the source code.

2. Install the required Python packages using pip:
   ```bash
   pip install streamlit easyocr pypdf2 pillow numpy
   ```

3. Ensure that the `craft_mlt_25k` model for EasyOCR is downloaded. EasyOCR will handle this automatically when you first run the application.

## Usage

1. Navigate to the directory containing the source code.
2. Run the Streamlit application using the following command:
   ```bash
   streamlit run app.py
   ```
3. The application will open in your default web browser. You can also access it via the URL provided in the terminal.

4. On the application page, you will see options to upload an image or a PDF file.

### Extract Text from Images

1. Click on the "Browse files" button under "Upload your image here" to upload an image file.
2. The uploaded image will be displayed on the page.
3. The application will process the image and display the extracted text below the image.

### Extract Text from PDFs

1. Click on the "Browse files" button under "Upload your PDF here" to upload a PDF file.
2. The application will process the PDF and display the extracted text on the page.

## Code Overview

### load_model

```python
def load_model(): 
    reader = ocr.Reader(['en'], model_storage_directory='.', gpu=False)
    return reader 
```
This function loads the EasyOCR model for English text recognition.

### extract_text_from_pdf

```python
def extract_text_from_pdf(file):
    output_text = ""
    reader = PyPDF2.PdfReader(file)
    for i in range(len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        output_text += current_text
    return output_text
```
This function extracts text from each page of a PDF file and concatenates it into a single string.

### Streamlit Application Logic

The application logic handles the file uploads and text extraction:

```python
st.title("Text from Images and PDFs")
st.markdown("## Extract Text From Image or PDF")

image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])
pdf = st.file_uploader(label="Upload your PDF here", type=['pdf'])

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

if pdf is not None:
    with st.spinner("Processing PDF..."):
        pdf_text = extract_text_from_pdf(pdf)
        st.write(pdf_text)
else:
    st.write("Upload a PDF")
```
This code displays the file upload options, processes the uploaded files, and displays the extracted text in the Streamlit application.

## License

This project is open source and available under the [MIT License](LICENSE).

---

Feel free to customize this README to better suit your specific project details and preferences.
