import streamlit as st
from PIL import Image, UnidentifiedImageError
import pytesseract
import os
import pyperclip
from plyer import notification
import time
import welcome

# Set your Tesseract path
tesseract_path = r'C:\Program Files\Tesseract-OCR'
#C:\Program Files\Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = os.path.join(tesseract_path, "tesseract.exe")

# Set Streamlit page configuration
st.set_page_config(
    page_title="TEXTEMAGE",
    page_icon="📃",
    layout="wide"
)

# Function to load image
def load_image(file):
    try:
        img = Image.open(file)
        return img
    except UnidentifiedImageError:
        st.error("Not a valid image file!")
        return None

# Function to perform OCR
def perform_ocr(img):
    try:
        result = pytesseract.image_to_string(img)
        return result
    except Exception as e:
        st.error(f"Error during text extraction: {str(e)}")
        return ""

# Main function
def main():

    if 'welcome_animation_shown' not in st.session_state:
        welcome.welcome_animation()
        st.session_state.welcome_animation_shown = True

    st.title("TEXTEMAGE - Image Text Extraction")
    st.write(
        "Upload an image, and TEXTEMAGE will extract the text content from it."
    )

    # Create a sidebar for additional information
    st.sidebar.markdown(
        """
        ### About TEXTEMAGE
        TEXTEMAGE is a simple Streamlit app for extracting text from images using Tesseract OCR.

        ##### How to Use
        1. Upload an image using the file uploader on the left.
        2. Click the 'Extract Text' button to perform OCR and see the extracted text on the right.
        3. Click the 'Copy Text' button to copy the extracted text to clipboard.
        4. Click the 'Download Text' button to download the extracted text.
        """
    )

    # Create two columns
    col1, space, col2 = st.columns([1, 0.3, 1])

    extracted_text = ""
    copied_text = ""
    download_text = ""
    flag = False

    # Column 1: Upload image box
    with col1:
        uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "bmp", "webp"])
        if uploaded_file is not None:
            img = load_image(uploaded_file)
            if img is not None:
                st.image(img, caption="Uploaded Image", use_column_width=True)

        if uploaded_file is not None and img is not None:

            col3, space, col4, space, col5 = st.columns([1, 0.1, 1, 0.1, 1])

            # Extract Text button
            with col3:
                if st.button("Extract Text", key="extract_button"):
                    extracted_text = perform_ocr(img)
                    copied_text = extracted_text
                    success_message = st.success("Text Extracted", icon="✅") 
                    time.sleep(0.5)
                    success_message.empty()
            
            # Copy Image button
            with col4:
                if st.button("Copy Image", key="copy_button"):
                    if copied_text == "":
                        copied_text = perform_ocr(img)
                    pyperclip.copy(copied_text)
                    success_message = st.success("Text copied", icon="✅") 
                    time.sleep(0.5)
                    success_message.empty()

            # Edit Image button
            with col5:
                if download_text == "":
                    download_text = perform_ocr(img)
                
                extracted_file_name = uploaded_file.name
                extracted_file_name = extracted_file_name.split(".")[0] + ".txt"
                
                if st.download_button(label="Download", data=download_text, file_name=extracted_file_name, mime="text/plain", key="download"):
                    success_message = st.success("Text downloaded", icon="✅") 
                    time.sleep(0.5)
                    success_message.empty()
                    flag = not flag

    # Column 2: Extracted or Copied text view
    with col2:
          
        # Apply Edited Text button

        if extracted_text:
            st.subheader("Extracted Text:")
            st.text_area("Extracted Text 👇", extracted_text, height=350)
            st.write("Text Extracted!")

        elif copied_text:
            st.subheader("Copied Text:")
            st.text_area("Copied Text 👇", copied_text, height=350)
            st.write("Text Copied in Clipboard!")
            pyperclip.copy(copied_text)

        elif flag:
            st.subheader("Downloaded Text:")
            st.text_area("Downloaded Text 👇", download_text, height=350)
            st.write("Text Download Completed as text.txt File!")

# Run the app
if __name__ == "__main__":
    main()

