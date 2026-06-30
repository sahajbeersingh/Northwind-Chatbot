from llm.model import ask_model
def get_llm_err(question,error):
    prompt = f"""
System:
You are an assistant for the Northwind Chatbot.

The chatbot failed to answer a user's question.

Your job is to explain the failure in simple, non-technical language.

Rules:
- keep response easy to understand that even a non technical person can understand
- Never mention HTTP status codes, OData, URLs, API endpoints, stack traces, or Python.
- Explain why the request could not be completed.
- If the requested entities cannot be combined because of schema limitations, say so.
- Keep the response under 2 sentences.

User Question:
{question}
Error:
{error}
    """
    response = ask_model([
        {
            "role": "system",
            "content": prompt
        }
    ])
    return response["choices"][0]["message"]["content"]

def get_error_message(error):
    error = str(error)
    if "ProxyError" in error:
        return "Unable to connect to the AI service. Please try again in a few moments."
    elif "ConnectTimeout" in error:
        return "The request timed out. Please try again."
    elif "JSONDecodeError" in error:
        return "The AI returned an unexpected response. Please try again."
    elif "404" in error:
        return "Requested resource not found."
    elif "401" in error:
        return "Authentication failed."
    elif "ConnectionError" in error:
        return "Unable to connect to the server."
    else:
        return "Something went wrong while processing your request."