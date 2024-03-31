import streamlit as st
import requests
from PIL import Image
import numpy as np
from inference.models.utils import get_roboflow_model
import cv2
import random
import time
import torch
from transformers import pipeline

text2text_generator = pipeline("text2text-generation")

##########
##### Set up sidebar.
##########


st.sidebar.write('#### Select an image to upload.')
uploaded_file = st.sidebar.file_uploader('',
                                         type=['png', 'jpg', 'jpeg'],
                                         accept_multiple_files=False)

##########
##### Set up main app.
##########

## Title.
st.write('# Pig Object Detection')
st.write('Please upload an image to the left to count the number of pigs in that image.')

## Pull in default image or user-selected image.
if uploaded_file is None:
    # Default image.
    st.write("Waiting...")
    url = 'https://images.unsplash.com/photo-1597092430872-09a3f4338c60?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2944&q=80'
    image = Image.open(requests.get(url, stream=True).raw)
    opencvImage = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
else:
    ## Pull user-selected image.
    image = Image.open(uploaded_file)
    opencvImage = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

## Subtitle.
st.write('### Inferenced Image')


model = get_roboflow_model(
    model_id="pig-count/1", 
    #Replace ROBOFLOW_API_KEY with your Roboflow API Key
    #api_key="ROBOFLOW_API_KEY"
    api_key="LxUviUVXkfaYWYXkBYcE"
)

results = model.infer(image=opencvImage,confidence=0.8,iou_threshold=0.85)

output=opencvImage.copy()
count=0

# Plot image with face bounding box (using opencv)
for result in results[0]:
    bounding_box = results[0][count]
    print(bounding_box)

    x0, y0, x1, y1 = map(int, bounding_box[:4])
        
    cv2.rectangle(output, (x0, y0), (x1, y1), (255,255,0), 2)
    cv2.putText(output, "Pig", (x0, y0 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    count=count+1

color_coverted = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

pil_image = Image.fromarray(color_coverted)

# Display image.
st.image(pil_image,
         use_column_width=True)


## Detection statements in main app.
st.write(f'### Number of Pigs Detected: {count}')

st.write("Welcome to the Question and Answer Chatbot. Let's talk about taking care of pigs.")
input = st.text_input("You detected " + str(count) +" pigs! Ask me something about them?")

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

