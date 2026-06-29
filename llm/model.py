import os
import requests
import streamlit as st
from dotenv import load_dotenv
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
    return response.json()
if __name__=="__main__":
    print(ask_model([{
        "role":"system",
        "content":" sayhello"
    }]))
