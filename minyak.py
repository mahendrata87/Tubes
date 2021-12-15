import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

st.set_page_config(layout="wide")
st.title("Analisis Data Produksi Minyak Dunia")

with open("kode_negara_lengkap.json") as f:
           data = json.load(f)
#for code in data:
           
#dfjson = pd.DataFrame.from_dict(data)
#country_name = df["name"].tolist()

#country = st.selectbox('Select Country:', 
#                       dfjson['name'])

#st.write('You selected:', country)
#for country_name in data:
#           data
#=====================================Plot1================================

kode='AUS'
df = pd.read_csv('produksi_minyak_mentah.csv')
dfc=df.drop(df.index[df['kode_negara'].isin(['WLD', 'G20','OECD'])])
dff = dfc.loc[dfc['kode_negara'] == kode]
plt.plot(dff['tahun'], dff['produksi'])

fig, ax = plt.subplots()
ax.plot(dff['tahun'], dff['produksi'])

st.pyplot(fig)

#====================================Plot2==================================
int_slide = st.slider('Tahun', min_value=1971, max_value=2015, value=1971, step=1)
int_num = st.number_input('Berapa Besar', min_value=1, max_value=15, value=5, step=1)
df2= dfc.loc[dfc['tahun'] == int_slide]
df3 = df2.sort_values(["produksi"], ascending=False)
df4 = df3.head(int(int_num))
#df5 = df4.merge(dfjson, left_on=['kode_negara'], right_on=["alpha-3"], how='inner')

fig2, axs = plt.subplots()
axs.bar(df4['kode_negara'], df4['produksi'])
st.pyplot(fig2)

#Plot3
df5 = dfc.head(int(int_num))
df6=df5.groupby('kode_negara', sort=False)['produksi'].sum().nlargest()
print(df6)
#fig3, axs3 = plt.subplots()
#axs3.bar(df6['kode_negara'], df6['produksi'])
#st.pyplot(fig3)
