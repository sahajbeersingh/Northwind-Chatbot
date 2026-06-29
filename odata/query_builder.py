import os
from dotenv import load_dotenv
load_dotenv()
Base_url=os.getenv("BASE_URL")

def build_query(query):
    entity=query["entity"]
    url=Base_url+entity
    if(query["top"]):
        if("?"not in url):
            url+="?"
        else:
            url+="&"
        url+="$top="+str(query["top"])
    if(query["orderby"]):
        if("?"not in url):
            url+="?"
        else:
            url+="&"
        url+="$orderby="+str(query["orderby"])
    if(query["filter"]):
        if("?"not in url):
            url+="?"
        else:
            url+="&"
        url+="$filter="+str(query["filter"])
    c=0
    for i in query["expand"]:
        if(c==0):
            if("?"not in url):
                url+="?"
            else:
                url+="&"
            url+="$expand="+i
            c=1
        else:
            url+=","+i
    c=0
    for i in query["select"]:
        if(c==0):
            if("?"not in url):
                url+="?"
            else:
                url+="&"
            url+="$select="+i
            c=1
        else:
            url+=","+i
    return url

if __name__ == "__main__":
    query = {
    "entity": "Products",
    "filter": "",
    "orderby": "",
    "top": None,
    "expand": [],
    "select": [
        "ProductName",
        "UnitPrice"
    ]
    }
    print(build_query(query))