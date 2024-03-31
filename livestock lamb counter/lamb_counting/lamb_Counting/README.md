# Pig Counting and Care Chatbot Application

This application integrates object detection with a chatbot to provide insights about pig care. Users can upload images to detect and count pigs, and then interact with the chatbot to learn more about taking care of them.

## Files Overview:

- **Pig_output.jpg**: Sample output image showcasing the result of the pig counting or object detection process.
  
- **chatbot.py**: Python script that showcases the chatbot functionality using Hugging Face Transformers.

- **pig.jpg**: Sample image of pigs that can be used for testing the object detection functionality.

- **pigs.txt**: Text file that contains information related to pigs.

- **app.py**: Main application script that integrates all functionalities and powers the web interface using Streamlit.

- **output.mov**: A video file, possibly showing the entire output/workflow of the application.

- **pig_counting_object_detection.py**: Python script to showcase the object detection and pig counting functionality.

- **requirements.txt**: Contains a list of Python libraries and dependencies required to run the application.

## Setup and Installation:

1. Clone the repository to your local machine.
   
2. Navigate to the project directory and install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the main application:
   ```
   streamlit run app.py
   ```

4. Open the provided link in your browser to interact with the application.

## Usage:

1. Upload an image of pigs using the sidebar.
2. View the object detection results and the number of pigs detected.
3. Interact with the chatbot to learn more about pig care.

## Future Enhancements:

- Improve the accuracy of the pig counting model.
- Expand the chatbot's knowledge base for a more comprehensive user experience.
- Integrate real-time video feed for continuous monitoring.

---
