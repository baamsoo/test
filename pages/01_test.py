import streamlit as st
from streamlit_folium import st_folium
import folium
import common

common.page_config()

st.title("Dot Map Visualization")

data = common.get_sales()

seoul = folium.Map(location=[37.55138077230307, 126.98712254969668], zoom_start=12)

folium.CircleMarker([37.4971850, 126.927595],
        radius=1,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6
    ).add_to(seoul)

folium.Marker([37.4971850, 126.927595], icon=folium.Icon(popup='Dongjak-gu', color='red', icon='glyphicon glyphicon-home')).add_to(seoul)

st_folium(seoul)
