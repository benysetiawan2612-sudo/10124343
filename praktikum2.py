import streamlit as st
import pandas as pd

st.title("Cek Judul dan Status SKP")

#Membaca data dari file Excel
df = pd.read_excel("data_skp.xlsx")

#Membuat kolom status (nilai default: 'LULUS')
df['status']='Lulus'

#Membuat kolom status_judul (cek apakah judul kosong atau ada)
df['status_judul'] = df['JUDUL'].apply(
    lambda x: 'Judul Kosong' if pd.isnull(x) or x == "" else 'Ada Judul'
)

#Menampilkan isi dataframe di Streamlit
st.subheader("Data SKP")
st.dataframe(df)