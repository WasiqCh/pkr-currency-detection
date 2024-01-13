# Importing the required libraries
import streamlit as st
from PIL import Image
from pk_currency_detector import currency


# Defining the title of the app
st.title('Pakistani Currency Detection')

# Defining the sidebar
st.sidebar.title('About Dev')
st.sidebar.info('This app is developed by Wasiq Nadeem, a 3rd Semester student of Computer Science at ARID University')
st.sidebar.title('About App')
st.sidebar.info('This is a simple app to detect the currency of a given image, The app is built using Tensorflow, Keras and Streamlit')
st.sidebar.title('How to use')
st.sidebar.info('Upload the image of the currency and the app will detect the currency')



# Defining the file uploader
uploaded_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])

# Checking if the file is uploaded
if uploaded_file is not None:
    # Reading the image
    image = Image.open(uploaded_file)

    # Displaying the image
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Checking if the user has clicked the button
    if st.button('Predict Currency'):
        # Calling the predict function
        label = currency(image)

        # Displaying the result
        st.success('The Prediction is: {}'.format(label))
            


