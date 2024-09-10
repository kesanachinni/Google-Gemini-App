import streamlit as st
import os
from streamlit_option_menu import  option_menu
working_dir=os.path.dirname(os.path.abspath(__file__))
from gemini_utility import (load_gemini_core_model,gemini_pro_vision_response,
                        gemini_pro_response,embedding_model_response)
from PIL import Image
# print(working_dir)
st.set_page_config(
    page_title='Gemini AI',
    page_icon='💡',
    layout="centered"
)

with st.sidebar:
    selected=option_menu("Gemini AI",
                         ["chatBot","image captioning","Embed Text","Ask any Question"],
                         menu_icon='robot',icons=['chat-dots-fill','textarea-t','patch-question-fill'],
                         default_index=0)
    
def translate_role_for_streamlit(user_role):
    if user_role=='model':
        return 'assistant'
    else:
        return 'user_role' 


if selected=='chatBot':
    
    model=load_gemini_core_model()
    if 'chat_session' not in st.session_state:
        st.session_state.chat_session=model.start_chat(history=[])
        
    st.title(" 🤖chat bot")
    
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)
    user_prompt=st.chat_input("Ask gemini pro...")
    
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        gemini_response=st.session_state.chat_session.send_message(user_prompt)  
        
        with st.chat_message('assistant'):
          st.markdown(gemini_response.text) 
          
     
if selected=='image captioning':
    st.title("🖼️ Gemini Vision Pro")
    
    upload_image=st.file_uploader("upload an image...", type=['jpg','jpeg','png'])
    if st.button("Generate content"):
        image=Image.open(upload_image)
        col1,col2=st.columns(2)
        with col1:
            resized_image=image.resize((800,500))
            st.image(resized_image)
            
        default_prompt='write a short caption for the image!'
        
        caption=gemini_pro_vision_response(default_prompt,image)
        with col2:
            st.info(caption)
            
            
if selected=='Embed Text':
    st.title("🖹 Embed Text")
    input_text=st.text_area(label="",placeholder='Enter the text to get the embeddings!')
    if(st.button("get Embeddings")):
        response=embedding_model_response(input_text)
        
        st.markdown(response)

if selected=="Ask any Question":
    st.title("🧐 Ask anything")
    user_prompt=st.text_area(label='',placeholder='Ask Gemini pro')
    
    if st.button('get answer'):
        response=gemini_pro_response(user_prompt)
        st.markdown(response)
        
    
    
            
            

        
              
    
              

    