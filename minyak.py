import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

st.set_page_config(layout="wide")
st.title("Aplikasi Analisis Data Produksi Minyak Mentah Dunia Tahun 1971 - 2015")
st.sidebar.title("Pengaturan")


with open("kode_negara_lengkap.json") as f:
           data = json.load(f)

#=====================================Plot1================================
st.header("Grafik Besar Produksi Minyak Mentah Setiap Negara per Tahun")
df = pd.read_csv('produksi_minyak_mentah.csv')
dfc=df.drop(df.index[df['kode_negara'].isin(['WLD', 'G20','OECD','OEU','EU28'])])
dfh = dfc
dfcode = dfh['kode_negara'].values.tolist()
dfnegara = list()

for country_code in dfcode:
           for country_name in data:
                      if country_code == country_name["alpha-3"]:
                                 country_code = country_name["name"]
           dfnegara.append(country_code)

dfh["kode_negara"] = dfnegara
dfr = dfh.sort_values(by=['kode_negara'], ascending=True)
df_baru = dfr.drop_duplicates('kode_negara')
select = st.selectbox('Select Country :',
                      (df_baru['kode_negara']))

groups = dfh.groupby(dfh['kode_negara'])
df_baru = groups.get_group(select)

negara = select

dff = df_baru.loc[df_baru['kode_negara'] == negara]
plt.plot(dff['tahun'], dff['produksi'])

fig, ax = plt.subplots()
ax.plot(dff['tahun'], dff['produksi'])
st.pyplot(fig)

#====================================Plot2==================================
st.header("Grafik Negara Penghasil Minyak Mentah Terbesar di Setiap Tahun")
int_slide = st.slider('Tahun :', min_value=1971, max_value=2015, value=1971, step=1)
int_num = st.number_input('Berapa Besar (untuk 2 grafik) :', min_value=1, max_value=15, value=5, step=1)
df2= dfc.loc[dfc['tahun'] == int_slide]
df3 = df2.sort_values(["produksi"], ascending=False)
df4 = df3.head(int(int_num))

fig2, axs = plt.subplots()
axs.bar(df4['kode_negara'], df4['produksi'])
st.pyplot(fig2)

imax = df3["produksi"].idxmax()
produksi_max = df3.loc[imax,'produksi']
negara_max = df3.loc[imax,'kode_negara']

i = 0
for kode in data:
    if negara_max == kode["name"]:
        st.write(data[i]["name"]+",",data[i]['alpha-3']+",",data[i]['region']+",",data[i]['sub-region'])
        st.write(produksi_max)
    i=i+1

#Plot3
st.header("Grafik Negara Penghasil Minyak Mentah Terbesar Kumulatif")
dfa = dfc.groupby(['kode_negara'], as_index=False)['produksi'].agg('sum')
dfb = dfa.sort_values(['produksi'],ascending=[0])
df5 = dfb.head(int(int_num))

fig3, axs3 = plt.subplots()
axs3.bar(df5['kode_negara'], df5['produksi'])
st.pyplot(fig3)
