from dotenv import load_dotenv
#loading all the environment variable
load_dotenv()

import streamlit as st
import os 
import google.generativeai as genai

genai.configure(api_key =os.getenv("GOOGLE_API_KEY"))

#creating func to load Gemini Pro model and  get response

model = genai.GenerativeModel("gemini-1.0-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#initializing the streamlit application

st.set_page_config(page_title ="Q&A Demo")

st.header("Gemini Application")

input = st.text_input("input" , key="input")

submit = st.button("Ask the Question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)