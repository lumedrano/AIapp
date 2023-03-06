import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel, pipeline


tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')


st.image("https://imageio.forbes.com/specials-images/imageserve/5ee2978b434cc00006720d80/0x0.jpg?format=jpg&width=1200")
st.title("AI Model - Luigi & Alex")

def generated_text(user_input):
    input_ids = tokenizer.encode(user_input, return_tensors='pt')
    
    output = model.generate(input_ids, 
                            max_length=150, 
                            temperature=0.6,
                            repetition_penalty=3.0,
                            top_k=50,
                            top_p=0.75,
                            do_sample=True  )
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text


user_input = st.text_input("Enter Prompt: ")

if st.button("Send"):
    st.write(generated_text(user_input))

