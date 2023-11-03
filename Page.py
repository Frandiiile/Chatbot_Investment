import streamlit as st
from process_message import process_message  # Import your process_message function

# Create a Streamlit app
st.title('Message Processor App')

# Define the Streamlit UI
message = st.text_input('Enter a message:')
if st.button('Process'):
    if message:
        result = process_message(message)  # Call your function
        st.write('Processed Message:', result)
    else:
        st.write('Please enter a message.')

# Run the Streamlit app
if __name__ == '__main__':
    st.write('Streamlit web app started.')
