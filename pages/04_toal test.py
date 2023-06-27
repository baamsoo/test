import streamlit as st
import common
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import pandas as pd



common.page_config()
st.title("PM10 Distribution by Top 5 Cities")

data1 = common.get_sales()

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
