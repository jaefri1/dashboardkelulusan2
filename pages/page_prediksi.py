import streamlit as st
import matplotlib.pyplot as plt

# Asumsikan model dan input_data sudah tersedia
prediction = model.predict(input_data)
probability = model.predict_proba(input_data)

st.subheader("Hasil Prediksi")

if prediction[0] == 1:
    st.success("### Mahasiswa diprediksi LULUS 🎉")
    st.write(f"Probabilitas: {probability[0][1]*100:.2f}%")
else:
    st.error("### Mahasiswa diprediksi TIDAK LULUS ❌")
    st.write(f"Probabilitas: {probability[0][0]*100:.2f}%")

# Visualisasi probabilitas
fig, ax = plt.subplots(figsize=(8, 3))
ax.barh(['Tidak Lulus', 'Lulus'], probability[0], color=['#ff6b6b', '#51cf66'])
ax.set_xlim(0, 1)
ax.set_xlabel('Probabilitas')
ax.set_title('Probabilitas Kelulusan')
st.pyplot(fig)

# Rekomendasi
st.subheader("Rekomendasi")
if prediction[0] == 0:
    st.write("""
    Berdasarkan prediksi, mahasiswa memiliki risiko tidak lulus. Berikut rekomendasi:
    - **Tingkatkan IPK**: Fokus pada mata kuliah dengan nilai rendah
    - **Kurangi mata kuliah tidak lulus**: Cari bantuan akademik untuk mata kuliah yang sulit
    - **Perbaiki kehadiran**: Tingkatkan frekuensi kehadiran di kelas
    - **Manajemen waktu**: Jika bekerja sambil kuliah, atur jadwal dengan lebih baik
    """)
else:
    st.write("""
    Prediksi menunjukkan mahasiswa memiliki potensi lulus. Untuk mempertahankan performa:
    - **Pertahankan IPK**: Lanjutkan kinerja akademik yang baik
    - **Pantau IPS tren**: Pastikan tren positif terus berlanjut
    - **Perhatikan beban kerja**: Jaga keseimbangan antara pekerjaan dan studi
    - **Persiapkan akhir studi**: Fokus pada penyelesaian tugas akhir atau skripsi
    """)
