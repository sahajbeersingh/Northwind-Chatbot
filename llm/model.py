import os
import requests
import streamlit as st
from dotenv import load_dotenv
class LLMException(Exception):
    pass
def ask_model(message):
    load_dotenv()
    try:
        api_key = st.secrets["MODEL_FARM_API_KEY"]
        url = st.secrets["URL"]
        model_name = st.secrets["MODEL"]
    except Exception:
        api_key = os.getenv("MODEL_FARM_API_KEY")
        url = os.getenv("URL")
        model_name = os.getenv("MODEL")
    try:
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
                },
                json={
                    "model": model_name,
                    "messages": message
                    }
            )
    except Exception as e:
        raise LLMException(str(e))
    return response.json()
if __name__=="__main__":
    print(ask_model([{
        "role":"system",
        "content":" sayhello"
    }]))
