import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel, pipeline

# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2LMHeadModel.from_pretrained('gpt2')


# st.image("https://imageio.forbes.com/specials-images/imageserve/5ee2978b434cc00006720d80/0x0.jpg?format=jpg&width=1200")
# st.title("AI Model - Luigi & Alex")

# st.text_input("Enter Prompt: ")



# Define an event listener that updates the cursor position
# def update_cursor_position():
#     st.session_state.cursor_position = st.get_last_cursor_position()

# # Create a text input field and add the event listener
# text_input = st.text_input('Type something here:', '', on_change=update_cursor_position)

# # Display the text input and the current cursor position
# st.write(f'You typed: {text_input}, Cursor position: {st.session_state.cursor_position}')


# Create a text input field
text_input = st.text_input('Type something here:', '')

# Display the text input and the current cursor position
st.write(f'You typed: {text_input}, Cursor position: {st.session_state.cursor_position}')
