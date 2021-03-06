#Syahrial Fitrachman 12220060
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
from PIL import Image

st.set_page_config(layout="wide")
st.title("Aplikasi Analisis Data Produksi Minyak Mentah Dunia")

st.sidebar.title('Selamat Datang !')
image = Image.open('oils.png')
st.sidebar.image(image)
st.sidebar.header('Aplikasi ini dibuat oleh:')
st.sidebar.markdown('Syahrial Fitrachman')
st.sidebar.markdown('NIM : 12220060')
st.sidebar.markdown('Jurusan Teknik Perminyakan')
st.sidebar.write('Institut Teknologi Bandung')
left_col, mid_col, right_col = st.columns(3)

df = pd.read_csv('produksi_minyak_mentah.csv')
dfc=df.drop(df.index[df['kode_negara'].isin(['WLD', 'G20','OECD','OEU','EU28'])])

with open("kode_negara_lengkap.json") as f:
           data = json.load(f)
data1 = pd.DataFrame.from_dict(data)
data2 = data1[['name', 'alpha-3','region','sub-region']]

st.subheader("List Negara dan Data Produksi")

dfcc = dfc.merge(data2, left_on='kode_negara', right_on='alpha-3', how='inner')
dfdata = dfcc[['name','kode_negara','tahun','produksi']]
st.dataframe(dfdata)

#==================================================== Plot1 ====================================================
st.header("Grafik Besar Produksi Minyak Mentah Setiap Negara per Tahun")

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

select = st.selectbox('Pilih Negara (N) :',
                      (df_baru['kode_negara']))

groups = dfc.groupby(dfc['kode_negara'])
df_baru = groups.get_group(select)

negara = select

dff = df_baru.loc[df_baru['kode_negara'] == negara]
plt.plot(dff['tahun'], dff['produksi'])

fig = plt.figure(figsize=(12, 5))
plt.plot(dff['tahun'], dff['produksi'])
plt.ylabel('Jumlah Produksi')
plt.xlabel('Tahun')
plt.grid()
st.pyplot(fig)

#==================================================== Plot2 ====================================================
st.header("Grafik Negara Penghasil Minyak Mentah Terbesar di Setiap Tahun")

int_slide = st.slider('Tahun (T) :', min_value=1971, max_value=2015, value=1971, step=1)
int_num = st.number_input('Berapa Besar (B) :', min_value=1, max_value=50, value=10, step=1)

df2= dfc.loc[dfc['tahun'] == int_slide]
df3 = df2.sort_values(["produksi"], ascending=False)
df4 = df3.head(int(int_num))

fig2 = plt.figure(figsize=(12, 5))
plt.bar(df4['kode_negara'], df4['produksi'])
plt.ylabel('Jumlah Produksi')
plt.xlabel('Negara')
plt.xticks(rotation='vertical')
st.pyplot(fig2)

#==================================================== Plot3 ====================================================
st.header("Grafik Negara Penghasil Minyak Mentah Terbesar Kumulatif")

int_number = st.number_input('Berapa Besar (B) :', min_value=1, max_value=55, value=10, step=1)

dfa = dfc.groupby(['kode_negara'], as_index=False)['produksi'].agg('sum')
dfb = dfa.sort_values(['produksi'],ascending=[0])
df5 = dfb.head(int(int_number))

fig3 = plt.figure(figsize=(12, 5))
plt.bar(df5['kode_negara'], df5['produksi'])
plt.ylabel('Total Produksi')
plt.xlabel('Negara')
plt.xticks(rotation='vertical')
st.pyplot(fig3)

#=================================================== Data Summary ==============================================
st.header("Data Summary")

int_slide2 = st.slider('Pilih Tahun (T) untuk Data Summary :', min_value=1971, max_value=2015, value=1971, step=1)

#Negara Penghasil minyak mentah terbesar pada tahun T
st.subheader("Data Negara Penghasil Minyak Mentah Terbesar pada Tahun (T)") 
st.write(int_slide2)

dfslide2= dfc.loc[dfc['tahun'] == int_slide2]
dfbig = dfslide2.sort_values(["produksi"], ascending=False)

imax = dfbig["produksi"].idxmax()
produksi_max = dfbig.loc[imax,'produksi']
negara_max = dfbig.loc[imax,'kode_negara']
i = 0

for kode in data:
    if negara_max == kode["name"]:
        #st.write("Data negara Penghasil minyak mentah pada tahun", int_slide,"adalah :") 
        st.write('Nama Negara :', data[i]["name"])
        st.write('Kode Negara :',data[i]['alpha-3'])
        st.write('Region      :',data[i]['region'])
        st.write('Sub-Region  :',data[i]['sub-region'])
        st.write("Dengan produksi minyak mentah sebesar = ", produksi_max)
    i=i+1

#Negara Penghasil minyak mentah terbesar kumulatif
st.subheader("Data Negara Penghasil Minyak Mentah Terbesar Kumulatif")

jmax = dfb["produksi"].idxmax()
produksi_jmax = dfb.loc[jmax,'produksi']
negara_jmax = dfb.loc[jmax,'kode_negara']
k = 0

for kode in data:
    if negara_jmax == kode["name"]:
        st.write('Nama Negara :', data[k]["name"])
        st.write('Kode Negara :',data[k]['alpha-3'])
        st.write('Region      :',data[k]['region'])
        st.write('Sub-Region  :',data[k]['sub-region'])
        st.write("Dengan produksi minyak mentah sebesar = ", produksi_jmax)
    k=k+1

#Negara Penghasil minyak mentah terkecil pada tahun T
st.subheader("Data Negara Penghasil Minyak Mentah Terkecil pada Tahun (T)") 
st.write(int_slide2)


dfst0 = dfslide2.sort_values(["produksi"], ascending=True)
dfmt0 = dfst0.loc[dfst0["produksi"] > 0]
imin = dfmt0["produksi"].idxmin()
produksi_min = dfmt0.loc[imin,'produksi']
negara_min = dfmt0.loc[imin,'kode_negara']
j = 0


for kode in data:
    if negara_min == kode["name"]: 
        st.write('Nama Negara :', data[j]["name"])
        st.write('Kode Negara :',data[j]['alpha-3'])
        st.write('Region      :',data[j]['region'])
        st.write('Sub-Region  :',data[j]['sub-region'])
        st.write("Dengan produksi minyak mentah sebesar = ", produksi_min)
    j=j+1
           
#Negara Penghasil minyak mentah terkecil kumulatif
st.subheader("Data Negara Penghasil Minyak Mentah Terkecil Kumulatif")
dfk = dfa.sort_values(['produksi'],ascending=[1])
dft = dfk.loc[dfk["produksi"] > 0]

jmin = dft["produksi"].idxmin()
produksi_jmin = dft.loc[jmin,'produksi']
negara_jmin = dft.loc[jmin,'kode_negara']
l = 0

for kode in data:
    if negara_jmin == kode["name"]:
        st.write('Nama Negara :', data[l]["name"])
        st.write('Kode Negara :',data[l]['alpha-3'])
        st.write('Region      :',data[l]['region'])
        st.write('Sub-Region  :',data[l]['sub-region'])
        st.write("Dengan produksi minyak mentah sebesar = ", produksi_jmin)
    l=l+1

#Negara yang Tidak Memproduksi Minyak pada Tahun T
st.subheader("Data Negara yang Tidak Memproduksi Minyak pada Tahun (T)") 
st.write(int_slide2)

df0 = dfslide2.loc[dfslide2["produksi"] == 0]
df_0 = df0.merge(data2, left_on='kode_negara', right_on='name', how='inner')
df__0 = df_0[['name', 'alpha-3','region','sub-region']]
df__0.rename(columns={'alpha-3': 'code'}, inplace=True)

st.dataframe(df__0)

#Negara yang Tidak Memproduksi Minyak
st.subheader("Data Negara yang Tidak Memproduksi Minyak") 

dfn0 = dfa.loc[dfa["produksi"] == 0]

df_n0=dfn0.merge(data2, left_on='kode_negara', right_on='name', how='inner')
dffinal = df_n0[['name', 'alpha-3','region','sub-region']]
dffinal.rename(columns={'alpha-3' : 'code', }, inplace=True)

st.dataframe(dffinal)
