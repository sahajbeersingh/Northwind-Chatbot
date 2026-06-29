from llm.model import ask_model

def generate_reasoning(question,query,df):
    prompt = f"""
You are a data analyst.

The user already has the data table displayed.

Rules:
1. Never repeat the entire table.
2. Never assume the data is sorted unless it is explicitly stated.
3. Never invent statistics or conclusions.
4. Use ONLY the provided data.
5. Keep the answer concise (under 120 words).

User Question:
{question}

Task:
{", ".join(query["instructions"]) if query["instructions"] else "Answer the user's question."}

Data:
{df.head(20).to_string(index=False)}
"""
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    response=ask_model(messages)
    return response["choices"][0]["message"]["content"]