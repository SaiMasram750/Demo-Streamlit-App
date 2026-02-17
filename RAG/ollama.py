from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
 #creating my prompt 
prompt =ChatPromptTemplate.from_messages(
  [
   ("system",'you are helpful assitant. please respond to the question asked'),
   ("user","Question:{question}")
  ]

 )

st.title('Langchain demo Chat App with genma3:1b')
input_text=st.text_input('what question do you have in mind')

llm =Ollama(model="gemma3:1b")
output_parser = StrOutputParser()
chain =prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

