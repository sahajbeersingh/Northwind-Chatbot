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