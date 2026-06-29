import requests
METADATA_URL = "https://services.odata.org/V4/Northwind/Northwind.svc/$metadata"
def refresh_metadata():
    response = requests.get(METADATA_URL)
    response.raise_for_status()
    with open("metadata/metadata.xml", "wb") as f:
        f.write(response.content)
if __name__=="__main__":
    refresh_metadata()