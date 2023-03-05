import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel, pipeline

# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2LMHeadModel.from_pretrained('gpt2')


# st.image("https://imageio.forbes.com/specials-images/imageserve/5ee2978b434cc00006720d80/0x0.jpg?format=jpg&width=1200")
# st.title("AI Model - Luigi & Alex")

# st.text_input("Enter Prompt: ")


# Load the text generation pipeline
generator = pipeline('text-generation', model='gpt2')

# Generate text
text = generator('Hello, how are you?', max_length=50)[0]['generated_text']

# Display the generated text on Streamlit
st.markdown(text)
