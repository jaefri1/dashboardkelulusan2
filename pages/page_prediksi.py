import streamlit as st
import numpy as np

def show_prediksi():
    st.title("🔮 Formulir Prediksi Kelulusan")

    st.write("Masukkan data untuk memprediksi apakah mahasiswa akan lulus:")

    umur = st.slider("Umur", 17, 35, 21)
    ipk = st.slider("IPK", 0.0, 4.0, 3.0, 0.01)
    sks = st.slider("Jumlah SKS", 0, 160, 110)

    if st.button("Prediksi"):
        if ipk >= 2.75 and sks >= 110:
            st.success("✅ Diprediksi: Lulus")
        else:
            st.error("❌ Diprediksi: Tidak Lulus")
