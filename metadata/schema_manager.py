import requests
import os
from dotenv import load_dotenv
load_dotenv()
Base_url=os.getenv("BASE_URL")
METADATA_URL = Base_url+"/$metadata"
def refresh_metadata():
    response = requests.get(METADATA_URL)
    response.raise_for_status()
    with open("metadata/metadata.xml", "wb") as f:
        f.write(response.content)
if __name__=="__main__":
    refresh_metadata()