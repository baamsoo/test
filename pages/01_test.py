import streamlit as st
from streamlit_folium import st_folium
import folium
import common

common.page_config()

st.title("Dot Map Visualization")

data = common.get_sales()

seoul = folium.Map(location=[37.55138077230307, 126.98712254969668], zoom_start=12)

# 위도 경도 DataFrame
location = df.groupby('Station code')['PM10'].agg([np.mean])
location['Latitude'] = df['Latitude'].unique()
location['Longitude'] = df['Longitude'].unique()

folium.Marker([37.4971850, 126.927595], icon=folium.Icon(popup='Dongjak-gu', color='red', icon='glyphicon glyphicon-home')).add_to(seoul)

st_folium(seoul)
