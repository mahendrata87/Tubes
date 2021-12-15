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
#dff = df.loc[df['kode_negara'] == kode]
#print(dff)
#plt.plot(dff['tahun'], dff['produksi'])

#fig, axs = plt.subplots()
#axs.plot(dff['tahun'], dff['produksi'])

#st.pyplot(fig)

int_slide = st.slider('Tahun', min_value=1971, max_value=2015, value=5, step=1)
int_num = st.number_input('Berapa Besar', min_value=1, max_value=15, value=5, step=1)
dff= df.loc[df['tahun'] == int_slide]
dff.sort_values(by=["produksi"], ascending=False)
dfff= dff.head(int_num)

fig, axs = plt.subplots()
axs.bar(dfff['kode_negara'], dfff['produksi'])

st.pyplot(fig)

st.write(int_slide)
st.write(int_num)
