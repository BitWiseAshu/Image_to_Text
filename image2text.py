# import streamlit as st
# from PIL import Image, UnidentifiedImageError
# import pytesseract
# # import os
# import pyperclip
# # from plyer import notification
# import time
# import welcome

# # # Set your Tesseract path
# # tesseract_path = r'C:\Users\Ashu\AppData\Local\Programs\Tesseract-OCR'
# # #C:\Program Files\Tesseract-OCR
# # pytesseract.pytesseract.tesseract_cmd = os.path.join(tesseract_path, "tesseract.exe")

# # Set Streamlit page configuration
# st.set_page_config(
#     page_title="TEXTEMAGE",
#     page_icon="📃",
#     layout="wide"
# )

# # Function to load image
# def load_image(file):
#     try:
#         img = Image.open(file)
#         return img
#     except UnidentifiedImageError:
#         st.error("Not a valid image file!")
#         return None

# # Function to perform OCR
# def perform_ocr(img):
#     try:
#         result = pytesseract.image_to_string(img)
#         return result
#     except Exception as e:
#         st.error(f"Error during text extraction: {str(e)}")
#         return ""

# # Main function
# def main():

#     if 'welcome_animation_shown' not in st.session_state:
#         welcome.welcome_animation()
#         st.session_state.welcome_animation_shown = True

#     st.title("TEXTEMAGE - Image Text Extraction")
#     st.write(
#         "Upload an image, and TEXTEMAGE will extract the text content from it."
#     )

#     # Create a sidebar for additional information
#     st.sidebar.markdown(
#         """
#         ### About TEXTEMAGE
#         TEXTEMAGE is a simple Streamlit app for extracting text from images using Tesseract OCR.

#         ##### How to Use
#         1. Upload an image using the file uploader on the left.
#         2. Click the 'Extract Text' button to perform OCR and see the extracted text on the right.
#         3. Click the 'Copy Text' button to copy the extracted text to clipboard.
#         4. Click the 'Download Text' button to download the extracted text.
#         """
#     )

#     # Create two columns
#     col1, space, col2 = st.columns([1, 0.3, 1])

#     extracted_text = ""
#     copied_text = ""
#     download_text = ""
#     flag = False

#     # Column 1: Upload image box
#     with col1:
#         uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "bmp", "webp"])
#         if uploaded_file is not None:
#             img = load_image(uploaded_file)
#             if img is not None:
#                 st.image(img, caption="Uploaded Image", use_column_width=True)

#         if uploaded_file is not None and img is not None:

#             col3, space, col4, space, col5 = st.columns([1, 0.1, 1, 0.1, 1])

#             # Extract Text button
#             with col3:
#                 if st.button("Extract Text", key="extract_button"):
#                     extracted_text = perform_ocr(img)
#                     copied_text = extracted_text
#                     success_message = st.success("Text Extracted", icon="✅") 
#                     time.sleep(0.5)
#                     success_message.empty()
            
#             # Copy Image button
#             with col4:
#                 if st.button("Copy Image", key="copy_button"):
#                     if copied_text == "":
#                         copied_text = perform_ocr(img)
#                     pyperclip.copy(copied_text)
#                     success_message = st.success("Text copied", icon="✅") 
#                     time.sleep(0.5)
#                     success_message.empty()

#             # Edit Image button
#             with col5:
#                 if download_text == "":
#                     download_text = perform_ocr(img)
                
#                 extracted_file_name = uploaded_file.name
#                 extracted_file_name = extracted_file_name.split(".")[0] + ".txt"
                
#                 if st.download_button(label="Download", data=download_text, file_name=extracted_file_name, mime="text/plain", key="download"):
#                     success_message = st.success("Text downloaded", icon="✅") 
#                     time.sleep(0.5)
#                     success_message.empty()
#                     flag = not flag

#     # Column 2: Extracted or Copied text view
#     with col2:
          
#         # Apply Edited Text button

#         if extracted_text:
#             st.subheader("Extracted Text:")
#             st.text_area("Extracted Text 👇", extracted_text, height=350)
#             st.write("Text Extracted!")

#         elif copied_text:
#             st.subheader("Copied Text:")
#             st.text_area("Copied Text 👇", copied_text, height=350)
#             st.write("Text Copied in Clipboard!")
#             pyperclip.copy(copied_text)

#         elif flag:
#             st.subheader("Downloaded Text:")
#             st.text_area("Downloaded Text 👇", download_text, height=350)
#             st.write("Text Download Completed as text.txt File!")

# # Run the app
# if __name__ == "__main__":
#     main()









# import streamlit as st
# from PIL import Image, UnidentifiedImageError
# import pytesseract
# import time
# import welcome

# # Set Streamlit page configuration
# st.set_page_config(
#     page_title="TEXTEMAGE",
#     page_icon="📃",
#     layout="wide"
# )

# # Function to load image
# def load_image(file):
#     try:
#         img = Image.open(file)
#         return img
#     except UnidentifiedImageError:
#         st.error("Not a valid image file!")
#         return None

# # Function to perform OCR
# def perform_ocr(img):
#     try:
#         result = pytesseract.image_to_string(img)
#         return result
#     except Exception as e:
#         st.error(f"Error during text extraction: {str(e)}")
#         return ""

# # Main function
# def main():
#     if 'welcome_animation_shown' not in st.session_state:
#         welcome.welcome_animation()
#         st.session_state.welcome_animation_shown = True

#     st.title("TEXTEMAGE - Image Text Extraction")
#     st.write("Upload an image, and TEXTEMAGE will extract the text content from it.")

#     # Create a sidebar for additional information
#     st.sidebar.markdown(
#         """
#         ### About TEXTEMAGE
#         TEXTEMAGE is a simple Streamlit app for extracting text from images using Tesseract OCR.

#         ##### How to Use
#         1. Upload an image using the file uploader on the left.
#         2. Click the 'Extract Text' button to perform OCR and see the extracted text on the right.
#         3. Click the 'Download Text' button to download the extracted text.
#         """
#     )

#     # Create two columns
#     col1, space, col2 = st.columns([1, 0.3, 1])

#     extracted_text = ""
#     download_text = ""
#     flag = False

#     # Column 1: Upload image box
#     with col1:
#         uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "bmp", "webp"])
#         if uploaded_file is not None:
#             img = load_image(uploaded_file)
#             if img is not None:
#                 st.image(img, caption="Uploaded Image", use_column_width=True)

#         if uploaded_file is not None and img is not None:

#             col3, space, col4 = st.columns([1, 0.1, 1])

#             # Extract Text button
#             with col3:
#                 if st.button("Extract Text", key="extract_button"):
#                     extracted_text = perform_ocr(img)
#                     download_text = extracted_text
#                     success_message = st.success("Text Extracted", icon="✅") 
#                     time.sleep(0.5)
#                     success_message.empty()

#             # Download button
#             with col4:
#                 if download_text == "":
#                     download_text = perform_ocr(img)
                
#                 extracted_file_name = uploaded_file.name
#                 extracted_file_name = extracted_file_name.split(".")[0] + ".txt"
                
#                 if st.download_button(label="Download", data=download_text, file_name=extracted_file_name, mime="text/plain", key="download"):
#                     success_message = st.success("Text downloaded", icon="✅") 
#                     time.sleep(0.5)
#                     success_message.empty()
#                     flag = not flag

#     # Column 2: Extracted or Downloaded text view
#     with col2:
#         if extracted_text:
#             st.subheader("Extracted Text:")
#             st.text_area("Extracted Text 👇", extracted_text, height=350)
#             st.write("Text Extracted!")

#         elif flag:
#             st.subheader("Downloaded Text:")
#             st.text_area("Downloaded Text 👇", download_text, height=350)
#             st.write("Text Download Completed as text.txt File!")

# # Run the app
# if __name__ == "__main__":
#     main()


















import streamlit as st
from PIL import Image, UnidentifiedImageError
import pytesseract
import time
import welcome

# Set Streamlit page configuration
st.set_page_config(
    page_title="TEXTEMAGE",
    page_icon="📃",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to improve the look and feel
st.markdown("""
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        color: #4A4A4A;
        font-size: 3rem !important;
        text-align: center;
        margin-bottom: 2rem !important;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3rem;
        font-size: 1rem;
        font-weight: bold;
    }
    .stTextArea>div>div>textarea {
        font-size: 1rem;
        border-radius: 5px;
    }
    .uploadedImage {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stAlert {
        background-color: #D4EDDA;
        color: #155724;
        border-color: #C3E6CB;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

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

    st.title("TEXTEMAGE")
    st.markdown("<p style='text-align: center; font-size: 1.2rem; margin-bottom: 2rem;'>Transform Your Images into Text with Ease</p>", unsafe_allow_html=True)

    # Create a sidebar for additional information
    with st.sidebar:
        st.markdown("## About TEXTEMAGE")
        st.info(
            "TEXTEMAGE is a powerful Streamlit app that extracts text from images using Tesseract OCR. "
            "Simply upload an image, and let TEXTEMAGE do the magic!"
        )
        st.markdown("### How to Use")
        st.markdown(
            "1. Upload an image using the file uploader.\n"
            "2. Click the 'Extract Text' button to perform OCR.\n"
            "3. View the extracted text on the right.\n"
            "4. Click the 'Download Text' button to save the extracted text."
        )

    # Create two columns
    col1, col2 = st.columns([1, 1])

    extracted_text = ""
    download_text = ""

    # Column 1: Upload image box
    with col1:
        st.markdown("### Upload Your Image")
        uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg", "bmp", "webp"])
        if uploaded_file is not None:
            img = load_image(uploaded_file)
            if img is not None:
                st.image(img, caption="Uploaded Image", use_column_width=True, output_format="PNG", clamp=True)
                st.markdown('<div class="uploadedImage"></div>', unsafe_allow_html=True)

        if uploaded_file is not None and img is not None:
            col3, col4 = st.columns(2)

            # Extract Text button
            with col3:
                if st.button("🔍 Extract Text", key="extract_button"):
                    with st.spinner("Extracting text..."):
                        extracted_text = perform_ocr(img)
                        download_text = extracted_text
                    st.success("Text Extracted Successfully!", icon="✅")

            # Download button
            with col4:
                if download_text == "":
                    download_text = perform_ocr(img)
                
                extracted_file_name = uploaded_file.name.split(".")[0] + ".txt"
                
                st.download_button(
                    label="📥 Download Text",
                    data=download_text,
                    file_name=extracted_file_name,
                    mime="text/plain",
                    key="download"
                )

    # Column 2: Extracted text view
    with col2:
        st.markdown("### Extracted Text")
        if extracted_text:
            st.text_area("Extracted content 👇", extracted_text, height=400)
        else:
            st.info("Upload an image and click 'Extract Text' to see the results here.")

# Run the app
if __name__ == "__main__":
    main()