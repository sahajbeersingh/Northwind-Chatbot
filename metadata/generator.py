import json
with open("metadata/schema.json")as f:
    schema=json.load(f)

def generate_context():
    context=""
    for entity,details in schema.items():
        context+=entity+"\n\n"
        context+="Primary Keys:\n"
        for field in details["primary_keys"]:
            context+=field+":"+details["properties"][field].replace("Edm.","")+"\n"
        context+="\nFields:\n"
        for field,typ in details["properties"].items():
            context+=field+":"+typ.replace("Edm.","")+"\n"
        context+="\nRelationships:\n"
        for field in details["navigation"]:
            context+=field+"\n"
        context+="\n----------------------\n"
    with open("metadata/context.txt","w",encoding="utf-8")as f:
        f.write(context)
if __name__=="__main__":
    generate_context()