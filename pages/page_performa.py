import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def show_performa():
    st.title("📈 Hasil Pelatihan Model")

    df = pd.read_csv("data/dataset_kelulusan_mahasiswa.csv")
    df['Lulus'] = df['Lulus'].map({'Ya': 1, 'Tidak': 0})

    X = df[['Umur', 'IPK', 'SKS']]
    y = df['Lulus']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    st.subheader("Laporan Klasifikasi")
    report = classification_report(y_test, y_pred, output_dict=True)
    st.dataframe(pd.DataFrame(report).transpose())
