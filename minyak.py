import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

st.set_page_config(layout="wide")
st.title("Analisis Data Produksi Minyak Dunia")

st.sidebar.title("Pengaturan")
left_col, mid_col, right_col = st.columns(3)

kode = 'AUS'
df = pd.read_csv('produksi_minyak_mentah.csv')
dff = df.loc[df['kode_negara'] == kode]
#print(dff)
plt.plot(dff['tahun'], dff['produksi'])
st.write(plt.show())
