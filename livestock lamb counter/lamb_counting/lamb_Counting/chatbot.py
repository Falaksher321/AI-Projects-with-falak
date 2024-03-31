import streamlit as st
import cv2
import random
import time
import torch
from transformers import pipeline

text2text_generator = pipeline("text2text-generation")

st.write("### Welcome to the Question and Answer Chatbot. Let's talk about taking care of pigs.")
input = st.text_input("Ask me something about pigs?")

if 'count' not in st.session_state or st.session_state.count == 6:
 st.session_state.count = 0 
 st.session_state.chat_history_ids = None
 st.session_state.old_response = ''
else:
 st.session_state.count += 1


if input:

    #read whole file to a string
    context_input= "Pigs need regular healthcare, including veterinary check-ups, vaccinations, and protection against diseases like swine flu and foot-and-mouth disease. They're social animals, so interaction with other pigs or humans is essential for their mental health. They also enjoy activities like playing with toys and listening to music, which enhance their well-being."

    response = text2text_generator('question: '+ input + 'context: ' +context_input)

    answer = response[0]['generated_text']
    print(answer)

    if answer == "":
        answer = "Sorry, I can't answer that."

    st.write(f"Chatbot: {answer}")
    st.session_state.old_response = answer

