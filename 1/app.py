from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')

# Configure Google's generative AI
genai.configure(api_key=google_api_key)

# Initialize Google's generative AI
genai_model = genai.GenerativeModel('gemini-pro')

# Streamlit configuration
st.set_page_config(page_title="Q&A Demo")

# Function to get response from Google's generative AI
def get_genai_response(question):
    response = genai_model.generate_content(question)
    return response.text

# Streamlit UI
st.header("Online Recipie Generator", anchor="top")
"Welcome to your Personel Recipie Generator chatbot app! Ask any question related to tasty recipies:"

input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the Question")

# When submit is clicked
if submit_button:
    response_text = get_genai_response(input_text)
    st.subheader("Response is ..")
    st.write(response_text)