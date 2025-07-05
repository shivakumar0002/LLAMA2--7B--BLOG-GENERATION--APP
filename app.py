import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

##Funciton to get response from the Llama 2model
def getLLamaresponse(input_text, no_words, blog_style):
    
        ### LLama2 model path
        llm = CTransformers(model='Model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                            model_type='llama',
                            config={'max_new_tokens': 256,
                                    'temperature': 0.01})
    
        # Prompt Template
        template = """
        write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words."""
    
        prompt = PromptTemplate(
            input_variables=["blog_style", "input_text", "no_words"],
            template=template
        )
    
        ## Generate the response from the LLama 2 model
        formatted_prompt = prompt.format(
            blog_style=blog_style,
            input_text=input_text,
            no_words=no_words
        )
        response = llm(formatted_prompt)
        print(response)
        return response


 


st.set_page_config(page_title="LLAMA 2 Chatbot", 
                   page_icon=":robot_face:", 
                   layout="centered", 
                   initial_sidebar_state="collapsed")
st.header("LLAMA 2 Chatbot")

input_text=st.text_input("Enter the blog topic")

## creating to more columns for the additional 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input("Enter the number of words to be generated")
    with col2:
        blog_style = st.selectbox('Writing the blog for',
                                  ('Researcher', 'data scientist', 'common people'), index=0)
                                
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))



