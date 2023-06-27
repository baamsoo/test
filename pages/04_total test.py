import streamlit as st
import common
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import pandas as pd

common.page_config()
st.title("PM10 Distribution by Top 5 Cities")

data1 = common.get_sales()

top_10 = pd.concat([PM10, PM2_5, SO2, NO2, O3, CO])

plt.style.use('fivethirtyeight')
fig,ax=plt.subplots(1,2,figsize=(15,8))
clr = ("blue", "forestgreen", "gold", "red", "purple",'cadetblue','hotpink','orange','darksalmon','brown')
top_10.Address.value_counts().sort_values(ascending=False)[:10].sort_values().plot(kind='barh',color=clr,ax=ax[0])
ax[0].set_title("Top 10 Cities",size=20)
ax[0].set_xlabel('Count',size=18)

count=top_10['Address'].value_counts()
groups=list(top_10['Address'].value_counts().index)[:10]
counts=list(count[:10])
counts.append(count.agg(sum)-count[:10].agg('sum'))
groups.append('Other')
type_dict=pd.DataFrame({"group":groups,"counts":counts})
clr1=('brown','darksalmon','orange','hotpink','cadetblue','purple','red','gold','forestgreen','blue','plum')
qx = type_dict.plot(kind='pie', y='counts', labels=groups,colors=clr1,autopct='%1.1f%%', pctdistance=0.9, radius=1.2,ax=ax[1])
plt.legend(loc=0, bbox_to_anchor=(1.15,0.4))
plt.subplots_adjust(wspace =0.5, hspace =0)
plt.ioff()
plt.ylabel('')

fig, ax = plt.subplots(figsize=(10,6))
sns.distplot(data1[data1.Address=='136, Hannam-daero, Yongsan-gu, Seoul, Republic of Korea'].PM10,color='maroon',hist=False,label='Hannam-daero')
sns.distplot(data1[data1.Address=='426, Hakdong-ro, Gangnam-gu, Seoul, Republic of Korea'].PM10,color='black',hist=False,label='Hakdong-ro')
sns.distplot(data1[data1.Address=='369, Yongmasan-ro, Jungnang-gu, Seoul, Republic of Korea'].PM10,color='blue',hist=False,label='Yongmasan-ro')
sns.distplot(data1[data1.Address=='49, Samyang-ro 139-gil, Gangbuk-gu, Seoul, Republic of Korea'].PM10,color='green',hist=False,label='Samyang-ro')
sns.distplot(data1[data1.Address=='43, Cheonho-daero 13-gil, Dongdaemun-gu, Seoul, Republic of Korea'].PM10,color='yellow',hist=False,label='Choenho-daero')
plt.title('PM10 Distribution by Top 5 Cities')
plt.legend(loc=0, bbox_to_anchor=(1.15,0.4))
plt.xlim(0,100)

st.pyplot(fig)
