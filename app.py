import streamlit as st
from query_rag import query_kcc

st.title("🌾 KCC Query Assistant")
user_query = st.text_input("Ask an agricultural question:")

if st.button("Get Answer") and user_query:
    with st.spinner("Thinking..."):
        response = query_kcc(user_query)
        st.success(response)
