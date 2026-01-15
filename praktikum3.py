import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Contoh Integrasi Folium + Streamlit")

#Titik peta indonesia
center_lat = -2.5489
center_lon = 118.0149

#Membuat peta folium
m = folium.Map(location=[center_lat, center_lon], zoom_start=5)

#Menampilkan di Streamlit
st_folium(m, width=700, height=500)