import streamlit as st
from core.pipeline import process_question
from utils.error_handler import get_error_message,get_llm_err
from llm.model import LLMException
import json
st.markdown("""
<style>
.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}
</style>
""", unsafe_allow_html=True)

with open("metadata/schema.json", encoding="utf-8") as f:
    schema = json.load(f)
st.set_page_config(
    page_title="Northwind Chatbot",
    page_icon="",
    layout="wide"
)

st.title("Northwind Chatbot")
st.caption("Natural language interface for the Northwind OData service")
with st.container(border=True):
    st.markdown("""
### 📌 Instructions

- Supports queries only on the **Northwind** database.
- Displays **one table** per query.
- Some complex relationships require **multiple queries**.
""")
with st.sidebar:
    st.header("Northwind Chatbot")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.subheader("Example Questions")

    examples = [
        "Show top 5 products",
        "Show products with supplier",
        "Show customers from Germany",
        "Show orders with customer",
        "Top 10 expensive products",
        "Show discontinued products"
    ]
    for q in examples:
        st.caption(q)

    st.divider()
    st.subheader("📊 Database Entities")
    for entity in sorted(schema.keys()):
        st.write(f">{entity}")

if "messages" not in st.session_state:
    st.session_state.messages = []
question = st.chat_input("Ask a question")
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.write(message["content"])
        else:
            if message["error"]:
                st.error(message["error"])
            if message["table"] is not None:
                st.dataframe(
                    message["table"],
                    width="stretch",
                    hide_index=True
                )
                if message["raw_json"]:
                    with st.expander("Raw Json"):
                        st.json(message["raw_json"])

            if message["reasoning"] is not None:
                st.subheader("Reasoning")
                st.write(message["reasoning"])

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    try:
        with st.spinner("Processing..."):
            response = process_question(question)
    except Exception as e:
        with st.spinner("Processing..."):
            if isinstance(e,LLMException):
                simplified_err=get_error_message(e)
            else:
                try:
                    simplified_err=get_llm_err(question,e)
                except:
                    simplified_err=get_error_message(e)
            response = {
                "table": None,
                "reasoning": None,
                "images": None,
                "error": simplified_err,
                "technical_details":str(e)
            }

    st.session_state.messages.append({
        "role": "assistant",
        "table": response.get("table"),
        "reasoning": response.get("reasoning"),
        "error": response.get("error"),
        "raw_json": response.get("raw_json")
    })

    with st.chat_message("assistant"):

        if response["error"]:
            st.error(response["error"])
            if "technical_details" in response:
                with st.expander("Technical Details"):
                    st.code(response["technical_details"])

        if response["table"] is not None:
            st.dataframe(
                response["table"],
                width="stretch",
                hide_index=True
            )
            if response["raw_json"] is not None:
                with st.expander("Raw Json"):
                    st.json(response["raw_json"])

        if response["reasoning"] is not None:
            st.subheader("Reasoning")
            st.write(response["reasoning"])