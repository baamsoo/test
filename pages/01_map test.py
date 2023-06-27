import streamlit as st
from streamlit_folium import st_folium
import folium
import common

common.page_config()

st.title("Dot Map Visualization")

data = common.get_sales()

seoul = folium.Map(location=[37.55138077230307, 126.98712254969668], zoom_start=12)

st_folium(seoul)
