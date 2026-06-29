import requests

def fetch_data(url):
    response=requests.get(url)
    response.raise_for_status()
    data=response.json()
    return data["value"]

if __name__=="__main__":

    url="https://services.odata.org/V4/Northwind/Northwind.svc/Products?$top=3&$expand=Supplier"
    records=fetch_data(url)
    print(records)