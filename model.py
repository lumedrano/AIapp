import streamlit as st
#from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
from transformers import BertForQuestionAnswering, BertTokenizer

# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2LMHeadModel.from_pretrained('gpt2')


bert_tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
bert_model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

# st.image("https://imageio.forbes.com/specials-images/imageserve/5ee2978b434cc00006720d80/0x0.jpg?format=jpg&width=1200")
# st.title("AI Model - Luigi & Alex")

# def generated_text(user_input):
#     input_ids = tokenizer.encode(user_input, return_tensors='pt')
    
#     output = model.generate(input_ids, 
#                             max_length=150, 
#                             temperature=0.6,
#                             repetition_penalty=3.0,
#                             top_k=50,
#                             top_p=0.75,
#                             do_sample=True)
#     generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
#     return generated_text



def question_answer(question, text):
    
    #tokenize question and text as a pair
    input_ids = bert_tokenizer.encode(question, text)
    
    #string version of tokenized ids
    tokens = bert_tokenizer.convert_ids_to_tokens(input_ids)
    
    #segment IDs
    #first occurence of [SEP] token
    sep_idx = input_ids.index(bert_tokenizer.sep_token_id)
    #number of tokens in segment A (question)
    num_seg_a = sep_idx+1
    #number of tokens in segment B (text)
    num_seg_b = len(input_ids) - num_seg_a
    
    #list of 0s and 1s for segment embeddings
    segment_ids = [0]*num_seg_a + [1]*num_seg_b
    assert len(segment_ids) == len(input_ids)
    
    #model output using input_ids and segment_ids
    output = bert_model(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]))
    
    #reconstructing the answer
    answer_start = torch.argmax(output.start_logits)
    answer_end = torch.argmax(output.end_logits)
    if answer_end >= answer_start:
        answer = tokens[answer_start]
        for i in range(answer_start+1, answer_end+1):
            if tokens[i][0:2] == "##":
                answer += tokens[i][2:]
            else:
                answer += " " + tokens[i]
                
    if answer.startswith("[CLS]"):
        answer = "Unable to find the answer to your question."
        return answer.capitalize()



# col1, col2 = st.columns([1,3])

# with col1:
#     preset = st.radio("Select one of our presets",
#                       ('Text Generation', 'Q&A'))
    
# with col2:
#     if preset == 'Text Generation':

#         user_input = st.text_input("Enter Prompt: ")

#         if st.button("Send"):
#             st.write(generated_text(user_input))
#     elif preset == 'Q&A':
#         text = st.text_area("Please enter your text: ")
#         question = st.text_input("Please enter your question: ")

#         if st.button('Send'):
#             st.write(question_answer(question, text))

text = input('Enter text: ')
if text:
    question = input('Enter question: ')
    if question:
        print(question_answer(question, text))

