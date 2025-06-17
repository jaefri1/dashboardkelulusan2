import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_eksplorasi():
    st.title("📊 Eksplorasi Dataset (EDA)")

    df = pd.read_csv("data/dataset_kelulusan_mahasiswa.csv")

    st.subheader("Cuplikan Data")
    st.dataframe(df)

    st.subheader("Distribusi Kelas")
    st.bar_chart(df['Lulus'].value_counts())

    st.subheader("Statistik Deskriptif")
    st.write(df.describe())

    st.subheader("Korelasi antar Fitur")
    corr = df.select_dtypes(include=['float64', 'int64']).corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
