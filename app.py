import streamlit as st 
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import PandasAI

st.set_page_config(layout='wide')
st.title("ChatCSV - Chat with your CSV files")

input_csv = st.file_uploader("Upload your CSV file here", type=['csv'])

if input_csv is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.info("CSV Uploaded Successfully")
        data = pd.read_csv(input_csv)
        st.dataframe(data, use_container_width=True)

    with col2:
        st.info("Chat Below")
        input_text = st.text_area("Enter your query")

        if input_text is not None:
            if st.button("Done"):
                st.info("Your Query: " + input_text)

                openai_api_key = st.secrets["my_secret"]["openai_api_key"]
                
                # Initialize OpenAI and PandasAI
                llm = OpenAI(api_token=openai_api_key)
                pandas_ai = PandasAI(llm)

                # Run chat_with_csv function
                result = pandas_ai.run(data, prompt=input_text)
                st.success(result)
