import streamlit as st
import openai
import pandas as pd
from get_clean_html import analyze_url, compose_message# <- import funkcji
from Save_Des_and_Key import Save_to_db
import openpyxl

st.title("Analiza strony HTML przez AI")

url = st.text_input("Podaj URL do przeanalizowania:")

if st.button("Analizuj stronę"):
    if not url:
        st.warning("Podaj poprawny URL.")
    else:
        with st.spinner("Pobieram i analizuję treść..."):
            try:
                result = analyze_url(url)
                st.subheader("Wynik analizy AI:")
                st.write(result)
                message = Save_to_db(url, result)
                st.write(message)
            except Exception as e:
                st.error(f"Wystąpił błąd: {e}")
