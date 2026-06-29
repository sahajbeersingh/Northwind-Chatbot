import requests
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
try:
    Base_url = st.secrets["BASE_URL"]
except Exception:
    Base_url = os.getenv("BASE_URL")
METADATA_URL = Base_url+"/$metadata"
def refresh_metadata():
    response = requests.get(METADATA_URL)
    response.raise_for_status()
    with open("metadata/metadata.xml", "wb") as f:
        f.write(response.content)
if __name__=="__main__":
    refresh_metadata()