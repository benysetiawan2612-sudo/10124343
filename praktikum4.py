import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Pie Chart Keilmuan SKP')

#Membaca data dari file Excel
df = pd.read_excel("data_skp.xlsx")

#Grup berdasarkan keilmuan
grouped = df.groupby('keilmuan')['JUDUL'].count().reset_index()

labels = grouped['keilmuan']
values = grouped['JUDUL']

#Plot pie chart
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
ax.set_title('Proporsi Judul Berdasarkan Keilmuan')

#Menampilkan pie chart ke Streamlit
st.pyplot(fig)

#Menampilksan tabel datanya
st.subheader("Tabel data per keilmuan")
st.dataframe(grouped)