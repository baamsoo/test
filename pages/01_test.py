import streamlit as st
from streamlit_folium import st_folium
import folium
import common
import numpy as np
from numpy import sin, cos, arccos, pi, round

common.page_config()

st.title("Dot Map Visualization")

data = common.get_sales()

seoul = folium.Map(location=[37.55138077230307, 126.98712254969668], zoom_start=12)

# 위도 경도 DataFrame
location = data.groupby('Station code')['PM10'].agg([np.mean])
location['Latitude'] = data['Latitude'].unique()
location['Longitude'] = data['Longitude'].unique()

markers = 999
loc_h = 0
loc_v = 0

for i in range(len(location)):
    folium.Circle(location=[location.iloc[i,1], location.iloc[i,2]], radius = location.iloc[i, 0]* 30, color=color_select(location.iloc[i,0]),fill_color='#ffffgg').add_to(seoul)
    if getDistanceBetweenPointsNew(37.4971850, 126.927595, location.iloc[i,1], location.iloc[i,2]) < markers :
        markers = getDistanceBetweenPointsNew(37.4971850, 126.927595, location.iloc[i,1], location.iloc[i,2])
        loc_h, loc_v = location.iloc[i,1], location.iloc[i,2]
    
folium.Marker([37.4971850, 126.927595], icon=folium.Icon(popup='Dongjak-gu', color='red', icon='glyphicon glyphicon-home')).add_to(seoul)
folium.Marker([loc_h, loc_v], icon=folium.Icon(popup='test', color='blue', icon='glyphicon glyphicon-home')).add_to(seoul)

st_folium(seoul)
