from llm.reasoning import generate_reasoning
def generate_response(question,query,df):
    response = {
        "table": None,
        "reasoning": None,
        "images": None,
        "error":None,
        "raw_json":None
    }
    if query["display"]["table"]:
        response["table"]=df
    if query["display"]["reasoning"]:
        response["reasoning"]=generate_reasoning(question,query,df)
    if query["display"]["image"]:
        response["image"]=None
    return response

if __name__=="__main__":
    print(generate_response())