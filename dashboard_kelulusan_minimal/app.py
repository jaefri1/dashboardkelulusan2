import streamlit as st
from pages.page_eksplorasi import show_eksplorasi
from pages.page_performa import show_performa
from pages.page_prediksi import show_prediksi

st.set_page_config(page_title="Dashboard Kelulusan", layout="wide")

st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Eksplorasi Dataset", "Performa Model", "Prediksi"])

if page == "Eksplorasi Dataset":
    show_eksplorasi()
elif page == "Performa Model":
    show_performa()
elif page == "Prediksi":
    show_prediksi()
