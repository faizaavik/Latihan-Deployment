import streamlit as st

# Fungsi untuk menghitung luas persegi
def hitung_luas_persegi(sisi):
    return sisi * sisi

st.title("Menghitung Luas Persegi dengan Form Input")

# Membuat form input
with st.form(key='form_luas_persegi'):
    sisi = st.number_input("Masukkan panjang sisi persegi (cm):", min_value=0.0, step=0.1)
    submit_button = st.form_submit_button(label='Hitung Luas')

# Jika tombol submit ditekan, tampilkan hasilnya
if submit_button:
    if sisi > 0:
        luas = hitung_luas_persegi(sisi)
        st.success(f"Luas persegi dengan sisi {sisi} cm adalah {luas} cm²")
    else:
        st.error("Sisi harus lebih dari 0")
