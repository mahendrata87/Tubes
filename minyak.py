import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

st.set_page_config(layout="wide")
st.title("Analisis Data Produksi Minyak Dunia")

st.sidebar.title("Pengaturan")
left_col, mid_col, right_col = st.columns(3)

kode = 'AUT'
df = pd.read_csv('produksi_minyak_mentah.csv')
dff = df.loc[df['kode_negara'] == kode]
#print(dff)
plt.plot(dff['tahun'], dff['produksi'])

fig, axs = plt.subplots()
axs.plot(dff['tahun'], dff['produksi'])

st.pyplot(fig)

user_input = st.text_input("Tahun = ")

int_val = st.slider('Seconds', min_value=1, max_value=10, value=5, step=1)
int_val = st.number_input('Seconds', min_value=1, max_value=10, value=5, step=1)
