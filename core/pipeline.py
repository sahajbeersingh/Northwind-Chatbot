from llm.query_understanding import understand_query
from odata.query_builder import build_query
from odata.client import fetch_data
from data.dataframe_processor import data_processor, frame_data
from metadata.refresh_manager import refresh_if_needed
from memory.session_manager import Session_Manager
from core.query_merger import merge_query
from response.response_generator import generate_response
session=Session_Manager()
def process_question(question):
    refresh_if_needed()
    session.add_user_message(question)
    query = understand_query(question,session.get_history(),session.get_last_query())
    if query["follow_previous"]:
        query=merge_query(session.get_last_query(),query)
    print(query)
    session.add_last_query(query)
    if query["intent"] == "OUT_OF_SCOPE":
        return {
            "table": None,
            "reasoning": None,
            "images": None,
            "error": query["message"]
        }
    if query["entity"] == "":
        return {
            "table": None,
            "reasoning": None,
            "images": None,
            "error": "No valid entity found"
        }
    url = build_query(query)
    records = fetch_data(url)
    raw_data = records
    cleaned = data_processor(records)
    df = frame_data(cleaned)
    session.add_last_dataframe(df)
    response=generate_response(question,query,df)
    response["raw_json"]=raw_data
    return response


if __name__=="__main__":
    print(process_question("hello"))