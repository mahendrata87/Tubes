import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

st.set_page_config(layout="wide")
st.title("Analisis Data Produksi Minyak Dunia")

with open("kode_negara_lengkap.json") as f:
           data = json.load(f)

#=====================================Plot1================================

kode='AUS'
df = pd.read_csv('produksi_minyak_mentah.csv')
dfc=df.drop(df.index[df['kode_negara'].isin(['WLD', 'G20','OECD'])])

dfcode = dfc['kode_negara'].values.tolist()
dfnegara = list()

for country_code in dfcode:
           for country_name in data:
                      if country_code == country_name["alpha-3"]:
                                 country_code = country_name["name"]
           dfnegara.append(country_code)
dfc["kode_negara"] = dfnegara
dfr = dfc.sort_values(by=['kode_negara'], ascending=True)
df_baru = dfr.drop_duplicates('kode_negara')
select = st.selectbox('Select Country :',
                      (df_new['kode_negara']))
negara = select

dff = df_baru.loc[df_baru['kode_negara'] == negara]
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
fig3, axs3 = plt.subplots()
axs3.bar(df6['kode_negara'], df6['produksi'])
st.pyplot(fig3)
