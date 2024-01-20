# Image to Text Converter

This project is a simple image-to-text converter implemented in Python. It provides a web application using Streamlit, with the ability to extract text from images using Tesseract OCR (Pytesseract). Additionally, Pyperclip is used for copying the extracted text to the clipboard, and Pillow is employed for image processing.

## Features

- Convert images to text
- Web application using Streamlit
- Tesseract OCR for text extraction
- Copy extracted text to the clipboard
- Image processing with Pillow

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Python
- Streamlit
- Pytesseract
- Pyperclip
- Pillow

## Clone the repository:
```bash
git clone https://github.com/Ashu-Pablo/Image_to_Text
cd Image_to_Text
```

## Make virutal environment
```python -m venev myenv```


## Activate virtual environment
```bash
# On Windows
myenv\Scripts\activate

# On macOS/Linux
source myenv/bin/activate
```

## Install dependencies:
```pip install -r requirements.txt```

## Download and Install Tesseract OCR
Download Tesseract OCR from https://github.com/UB-Mannheim/tesseract/wiki and install it on your local machine.

After installation, copy your Tesseract OCR path. Update line 10 in `image2text.py`:
```python
tesseract_path = r'C:\Users\(your)\AppData\Local\Programs\Tesseract-OCR'
#or
tesseract_path = r'C:\Program Files\Tesseract-OCR'
```

## Run Streamlit
```bash
streamlit run image2text.py 
```
Open your web browser and go to http://localhost:8501 to access the application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize the instructions further based on your specific project details or requirements.

