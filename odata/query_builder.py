import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
try:
    Base_url = st.secrets["BASE_URL"]
except Exception:
    Base_url = os.getenv("BASE_URL")
def build_expand(expands):
    tree = {}
    for path in expands:
        parts = path.split("/")
        current = tree
        for part in parts:
            current = current.setdefault(part, {})
    return ",".join(convert_tree(tree))
def convert_tree(tree):
    result = []
    for node, children in tree.items():
        if children:
            nested = ",".join(convert_tree(children))
            result.append(f"{node}($expand={nested})")
        else:
            result.append(node)
    return result
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
    if query["expand"]:
        if "?" not in url:
            url += "?"
        else:
            url += "&"
        url += "$expand=" + build_expand(query["expand"])
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