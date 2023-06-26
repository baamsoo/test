import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from numpy import sin, cos, arccos, pi, round
# !pip install folium -q
# pip install streamlit pandas numpy folium
import folium # 지도 관련
from folium import Marker
from folium import plugins
from folium import GeoJson
from folium.plugins import MarkerCluster
from datetime import datetime
import plotly.graph_objects as go

# df = pd.read_csv(
#     "https://raw.githubusercontent.com/baamsoo/test/main/Measurement_summary.csv"
# )


# def rad2deg(radians):
#     degrees = radians * 180 / pi
#     return degrees

# def deg2rad(degrees):
#     radians = degrees * pi / 180
#     return radians

# def getDistanceBetweenPointsNew(latitude1, longitude1, latitude2, longitude2):
    
#     theta = longitude1 - longitude2
    
#     distance = 60 * 1.1515 * rad2deg(
#         arccos(
#             (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) + 
#             (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
#         )
#     )

#     return round(distance * 1.609344, 2)


# # 위도 경도 DataFrame
# location = df.groupby('Station code')['PM10'].agg([np.mean])
# location['Latitude'] = df['Latitude'].unique() # 절대 이렇게 코드짜면 안되요!
# location['Longitude'] = df['Longitude'].unique()

# # PM10에 따른 color 변화
# def color_select(x):
#     if x >= 45:
#         return 'red'
#     elif x >= 40:
#         return 'yellow'
#     else:
#         return 'blue'

# # Map
# seoul = folium.Map(location=[37.55138077230307, 126.98712254969668], zoom_start=12)

# markers = 999
# loc_h = 0
# loc_v = 0

# # Circle
# for i in range(len(location)):
#     # 관측소
#     folium.Circle(location=[location.iloc[i,1], location.iloc[i,2]], radius = location.iloc[i, 0]*30, color=color_select(location.iloc[i,0]),fill_color='#ffffgg').add_to(seoul)
#     if getDistanceBetweenPointsNew(37.4971850, 126.927595, location.iloc[i,1], location.iloc[i,2]) < markers :
#         markers = getDistanceBetweenPointsNew(37.4971850, 126.927595, location.iloc[i,1], location.iloc[i,2])
#         loc_h, loc_v = location.iloc[i,1], location.iloc[i,2]


# # Marker / Sejong Univ.
# folium.Marker([37.4971850, 126.927595], icon=folium.Icon(popup='Dongjak-gu', color='red', icon='glyphicon glyphicon-home')).add_to(seoul)
# folium.Marker([loc_h, loc_v], icon=folium.Icon(popup='test', color='blue', icon='glyphicon glyphicon-home')).add_to(seoul)


# seoul


@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/baamsoo/test/main/Measurement_summary.csv"
    df = pd.read_csv(url)
    return df

def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees

def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians

def getDistanceBetweenPointsNew(latitude1, longitude1, latitude2, longitude2):
    theta = longitude1 - longitude2
    distance = 60 * 1.1515 * rad2deg(
        acos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) + 
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )
    return round(distance * 1.609344, 2)

def color_select(x):
    if x >= 45:
        return 'red'
    elif x >= 40:
        return 'yellow'
    else:
        return 'blue'

@st.cache
def create_map(df):
    location = df.groupby('Station code')['PM10'].mean().reset_index()
    location['Latitude'] = df.groupby('Station code')['Latitude'].mean().values
    location['Longitude'] = df.groupby('Station code')['Longitude'].mean().values

    seoul = folium.Map(location=[37.55138077230307, 126.98712254969668], zoom_start=12)

    markers = 999
    loc_h = 0
    loc_v = 0

    for i in range(len(location)):
        folium.Circle(
            location=[location.iloc[i, 2], location.iloc[i, 3]],
            radius=location.iloc[i, 1] * 30,
            color=color_select(location.iloc[i, 1]),
            fill_color='#ffffgg'
        ).add_to(seoul)

        if getDistanceBetweenPointsNew(37.4971850, 126.927595, location.iloc[i, 2], location.iloc[i, 3]) < markers:
            markers = getDistanceBetweenPointsNew(37.4971850, 126.927595, location.iloc[i, 2], location.iloc[i, 3])
            loc_h, loc_v = location.iloc[i, 2], location.iloc[i, 3]

    folium.Marker([37.4971850, 126.927595], icon=folium.Icon(popup='Dongjak-gu', color='red', icon='glyphicon glyphicon-home')).add_to(seoul)
    folium.Marker([loc_h, loc_v], icon=folium.Icon(popup='test', color='blue', icon='glyphicon glyphicon-home')).add_to(seoul)

    return seoul

df = load_data()
map_data = create_map(df)

st.markdown('<h1>Seoul Air Quality Map</h1>', unsafe_allow_html=True)
st.markdown(map_data._repr_html_(), unsafe_allow_html=True)
