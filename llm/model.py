import os
import requests
import streamlit as st
from dotenv import load_dotenv
print("Importing llm.model")
# def ask_model(message):
#     load_dotenv()
#     try:
#         api_key = st.secrets["MODEL_FARM_API_KEY"]
#         url = st.secrets["URL"]
#         model_name = st.secrets["MODEL"]
#     except Exception:
#         api_key = os.getenv("MODEL_FARM_API_KEY")
#         url = os.getenv("URL")
#         model_name = os.getenv("MODEL")
#     print("Calling ask_model")
#     response = requests.post(
#         url,
#         headers={
#             "Authorization": f"Bearer {api_key}",
#             "Content-Type": "application/json"
#             },
#             json={
#                 "model": model_name,
#                 "messages": message
#                 }
#         )
#     print("Status:", response.status_code)
#     print(response.text[:500])
#     return response.json()

def ask_model(message):
    return {
        "choices": [
            {
                "message": {
                    "content": '{"follow_previous": false, "intent": "OUT_OF_SCOPE", "entity": "", "message": "Test"}'
                }
            }
        ]
    }
if __name__=="__main__":
    print(ask_model([{
        "role":"system",
        "content":" sayhello"
    }]))
