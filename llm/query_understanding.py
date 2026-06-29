from llm.model import ask_model
from memory.session_manager import Session_Manager
import json
with open("metadata/context.txt","r",encoding="utf-8")as f:
    context=f.read()
with open("prompts/examples.txt","r",encoding="utf-8")as f:
    examples=f.read()
with open("prompts/system_prompt.txt","r",encoding="utf-8")as f:
    sys_prompt=f.read()

def understand_query(question,history,last_query):
    if history==None:
        history=[]
    message=[]
    if last_query is not None:
        message.append({
            "role":"system",
            "content":"previous Query=\n"+json.dumps(last_query, indent=2)
        })
    message.append({
        "role":"system",
        "content":context
    })
    message.append({
        "role":"system",
        "content":examples
    })
    message.append({
        "role":"system",
        "content":sys_prompt
    })
    message.extend(history)
    message.append({
        "role":"user",
        "content":question
    })
    response=ask_model(message)
    content = response["choices"][0]["message"]["content"]

    return json.loads(content)

if __name__ == "__main__":
    res=understand_query(
        "what is python",[]
    )
    print(res)
    print(type(res))