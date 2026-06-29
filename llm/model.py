import os
import requests
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("MODEL_FARM_API_KEY")
url=os.getenv("URL")
model_name=os.getenv("MODEL")
def ask_model(message):
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
