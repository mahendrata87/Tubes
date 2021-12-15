import streamlit as st

st.set_page_config(layout="wide")
st.title("Analisis Data Produksi Minyak Dunia")

st.sidebar.title("Pengaturan")
left_col, mid_col, right_col = st.columns(3)

st.sidebar.subheader("Pengaturan konfigurasi tampilan")
