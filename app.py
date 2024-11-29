#import relevant packages
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from myPrompts import *
import re

#------------------------------------------------------------------------------------------------
#initialize the model
#------------------------------------------------------------------------------------------------
def modelIntializer(params):
    model = OllamaLLM(
        model='llama3.2:latest',
        **params
    )
    return model


#------------------------------------------------------------------------------------------------
# create an title of the web app
#------------------------------------------------------------------------------------------------
st.title("Multi-Task Language Assistant Web Application")


#------------------------------------------------------------------------------------------------
#create a side bar that users can select option for task type
#------------------------------------------------------------------------------------------------
task = st.sidebar.selectbox(label='Select task type', 
                     options=['Text summarization', 'Language translation', 'Sentiment Analysis',
                     'Question answering', 'Entity recognition'])



#------------------------------------------------------------------------------------------------
# define process for text summarization
#------------------------------------------------------------------------------------------------
if task == 'Text summarization':
    #initialize the model with the right sets of hyper-parameters for text summariation
    params = {'temperature': 0.8}
    model = modelIntializer(params)

    # get the prompt template
    prompt = ChatPromptTemplate.from_template(textSummarizationTemplate)

    # init the chain
    chain = prompt | model

    text = st.chat_input("Message LlamaGPT")
    if text:
        st.chat_message("user").markdown(text)
        
        #get the model response
        response = chain.invoke({"text": text})

        # clean the response
        response = re.sub(r"\*.*?!\*", "", response)

        #display the response from the AI
        st.chat_message('ai').markdown(response)


#------------------------------------------------------------------------------------------------
# define process for sentiment analysis
#------------------------------------------------------------------------------------------------
if task == 'Sentiment Analysis':
    #initialize the model with the right sets of hyper-parameters for text summariation
    params = {'temperature': 0.001, 'max_tokens':2}
    model = modelIntializer(params)

    # get the prompt template
    prompt = ChatPromptTemplate.from_template(sentAnalysisTemplate)

    # init the chain
    chain = prompt | model

    text = st.chat_input("Message LlamaGPT")
    if text:
        st.chat_message("user").markdown(text)
        
        #get the model response
        response = chain.invoke({"feedback": text})

        # clean the response
        # response = re.sub(r"\*.*?!\*", "", response)

        #display the response from the AI
        st.chat_message('ai').markdown(response)




#------------------------------------------------------------------------------------------------
# define process for language translation
#------------------------------------------------------------------------------------------------
if task == 'Language translation':
    #initialize the model with the right sets of hyper-parameters for text summariation
    params = {'temperature': 1.0}
    model = modelIntializer(params)

    # get the prompt template
    prompt = ChatPromptTemplate.from_template(lanTranslationTemplate)

    # init the chain
    chain = prompt | model

    # get the first languages
    firstLanguage = st.selectbox(
        label='From',
        options=['French', 'Swahili', 'Korean', 'English', 'Spanish', 'Italian']
    )
    # get the second languages
    secondLanguage = st.selectbox(
        label='To',
        options=['French', 'Swahili', 'Korean', 'English', 'Spanish', 'Italian']
    )

    text = st.chat_input("Message LlamaGPT")

    if text:
        st.chat_message("user").markdown(text)
        
        #get the model response
        response = chain.invoke({"language1": firstLanguage, "language2":secondLanguage,
        "text": text})

        # clean the response
        response = re.sub(r"\*.*?!\*", "", response)

        #display the response from the AI
        st.chat_message('ai').markdown(response)


#------------------------------------------------------------------------------------------------
# define process for Question Answering
#------------------------------------------------------------------------------------------------
if task == 'Question answering':
    #initialize the model with the right sets of hyper-parameters for text summariation
    params = {'temperature': 0.8}
    model = modelIntializer(params)

    # get the prompt template
    prompt = ChatPromptTemplate.from_template(qATemplate)

    # init the chain
    chain = prompt | model

    text = st.chat_input("Message LlamaGPT")
    if text:
        st.chat_message("user").markdown(text)
        
        #get the model response
        response = chain.invoke({"question": text})

        # clean the response
        response = re.sub(r"\*.*?!\*", "", response)

        #display the response from the AI
        st.chat_message('ai').markdown(response)


#------------------------------------------------------------------------------------------------
# define process for Entity recognition
#------------------------------------------------------------------------------------------------
if task == 'Entity recognition':
    #initialize the model with the right sets of hyper-parameters for text summariation
    params = {'temperature': 0.5}
    model = modelIntializer(params)

    # get the prompt template
    prompt = ChatPromptTemplate.from_template(entityRecogTemplate)

    # init the chain
    chain = prompt | model

    text = st.chat_input("Message LlamaGPT")
    if text:
        st.chat_message("user").markdown(text)
        
        #get the model response
        response = chain.invoke({"transcript": text})

        # clean the response
        response = re.sub(r"\*.*?!\*", "", response)

        #display the response from the AI
        st.chat_message('ai').markdown(response)
