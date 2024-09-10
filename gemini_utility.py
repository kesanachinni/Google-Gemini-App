
# def load_gemini_core_model():
#     gemini_pro_model=genai.GenerativeModel("gemini.pro")
#     return gemini_pro_model

import os
from PIL import Image 
import google.generativeai as genai
import json

# Get the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load the config file
config_path=f'{working_dir}/config.json'

config_data=json.load(open(config_path))
GOOGLE_API_KEY=config_data['GOOGLE_API_KEY']

genai.configure(api_key=GOOGLE_API_KEY)
# function for chatbot
def load_gemini_core_model():
  model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")
  # print(response.text)
  return model

# function for image captioning
def gemini_pro_vision_response(prompt,image):
  gemini_pro_vision_model=genai.GenerativeModel('gemini-1.5-flash')
  
  response=gemini_pro_vision_model.generate_content([prompt,image]) 
  result=response.text
  return result


# prompt="caption the image"
# image=Image.open('test_image.png')
# res=gemini_pro_vision_response(prompt,image) 

# print(res)


def embedding_model_response(input_text):
  embedding_model='models/embedding-001'
  embedding=genai.embed_content(model=embedding_model,content=input_text,task_type="retrieval_document")
  embedding_list=embedding['embedding']
  return embedding_list

# res=embedding_model_response("who is PM of india")
# print(res)


def gemini_pro_response(user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    response=model.generate_content(user_input)
    
    res=response.text
    return res
  
  
res=gemini_pro_response("what is AI")
    
print(res)
    
    
    
  