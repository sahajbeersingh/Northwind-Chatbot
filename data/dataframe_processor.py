import pandas as pd
def flatten_dict(row,data,main):
    for key,val in data.items():
        if isinstance(val, dict):
            row=flatten_dict(row,val,main+"."+key)
        elif not key.startswith('@odata'):
            nk=main+"."+key
            row[nk]=val
    return row

def frame_data(data):
    df=pd.DataFrame(data)
    return df

def data_processor(data):
    cleaned=[]
    for i in data:
        new_row={}
        for key,val in i.items():
            if isinstance(val, dict):
                new_row=flatten_dict(new_row,val,key)
            elif not key.startswith('@odata'):
                new_row[key]=val
        cleaned.append(new_row)
    return cleaned

if __name__=="__main__":
    dt=dt = [
    {
        "ProductID": 1,
        "ProductName": "Chai",

        "Supplier": {
            "SupplierID": 1,
            "CompanyName": "Exotic Liquids",

            "Address": {
                "Street": "49 Gilbert St.",
                "City": "London",

                "Location": {
                    "Latitude": 51.5074,
                    "Longitude": -0.1278
                }
            }
        }
    }
]
    print(frame_data(data_processor(dt)))