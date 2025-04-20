import google.generativeai as genai
import streamlit as st
import os
import PIL.Image  

from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-001")


def get_gemini_response(image, input):
    if input:
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini application")
input_prompt = st.text_input("Input Prompt: ", key="input")

# Create a file uploader that accepts images
uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])

# Check if a file is uploaded
if uploaded_file is not None:
    file_name = uploaded_file.name

    if file_name.endswith('.png') or file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
        try:
            image = PIL.Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)

            submit = st.button("Analyze Image")

            # Submit button clicked and image uploaded
            if submit:
                # Pass input_prompt here
                response = get_gemini_response(image, input_prompt)  
                st.subheader("The response is:")
                st.write(response)
        except (IOError, ValueError) as e:
            st.error(f"Error processing image: {e}")
    else:
        st.warning("Please upload a PNG, JPG, or JPEG image.")