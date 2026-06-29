import copy
def merge_query(prev,curr):
    merged=copy.deepcopy(prev)
    ow_fields=["intent", "entity", "filter", "orderby", "top", "message"]
    for field in ow_fields:
        if field not in merged.keys():
            continue
        val=curr.get(field)
        if field == "intent" and val == "FOLLOW_UP":
            continue
        if val not in ("",[],None):
            merged[field]=val
    for item in curr.get("expand",[]):
        merged["expand"].append(item)
    for item in curr.get("select",[]):
        merged["select"].append(item)
    for item in curr.get("instructions",[]):
        merged["instructions"].append(item)
    for key,val in curr.get("display",{}).items():
        merged["display"][key]=val
    merged["follow_previous"]=False
    return merged

if __name__=="__main__":
    previous = {
        "follow_previous": False,
        "intent": "DATA_RETRIEVAL",
        "entity": "Products",
        "filter": "",
        "orderby": "",
        "top": 5,
        "expand": ["id"],
        "select": [],
        "display": {
            "table": True,
            "image": False,
            "chart": False,
            "reasoning": False
        },
        "instructions": []
    }
    current = {
        "follow_previous": True,
        "intent": "DATA_RETRIEVAL",
        "entity": "",
        "filter": "Discontinued eq true",
        "orderby": "UnitPrice desc",
        "top": 2,
        "expand": ["val"],
        "select": [],
        "display": {"reasoning": True},
        "instructions": [],
        "message":""
    }
    print(merge_query(previous,current))