import streamlit as st
from streamlit_folium import st_folium
import folium
import common

common.page_config()

st.title("Dot Map Visualization")

data = common.get_sales()

seoul = folium.Map(location=[37.55138077230307, 126.98712254969668], zoom_start=12)

# 데이터 시각화
for idx, row in data.iterrows():
    lat, lon = row['Latitude'], row['Longitude']
    
    # CircleMarker를 사용하여 도트맵 표현
    folium.CircleMarker(
        location=[lat, lon],
        radius=1,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6
    ).add_to(seoul)


st_folium(seoul)
