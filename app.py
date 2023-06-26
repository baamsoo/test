import pandas as pd
import numpy as np
import seaborn as sns
from numpy import sin, cos, arccos, pi, round
!pip install folium -q
import folium # 지도 관련
from folium import Marker
from folium import plugins
from folium import GeoJson
from folium.plugins import MarkerCluster
from datetime import datetime
import plotly.graph_objects as go

df = pd.read_csv(
    "https://raw.githubusercontent.com/baamsoo/test/main/Measurement_summary.csv"
)
df


def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees

def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians

def getDistanceBetweenPointsNew(latitude1, longitude1, latitude2, longitude2):
    
    theta = longitude1 - longitude2
    
    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) + 
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )

    return round(distance * 1.609344, 2)


# 위도 경도 DataFrame
location = df.groupby('Station code')['PM10'].agg([np.mean])
location['Latitude'] = df['Latitude'].unique() # 절대 이렇게 코드짜면 안되요!
location['Longitude'] = df['Longitude'].unique()
location.head()

# PM10에 따른 color 변화
def color_select(x):
    if x >= 45:
        return 'red'
    elif x >= 40:
        return 'yellow'
    else:
        return 'blue'

# Map
seoul = folium.Map(location=[37.55138077230307, 126.98712254969668], zoom_start=12)

markers = 999
loc_h = 0
loc_v = 0

# Circle
for i in range(len(location)):
    # 관측소
    folium.Circle(location=[location.iloc[i,1], location.iloc[i,2]], radius = location.iloc[i, 0]*30, color=color_select(location.iloc[i,0]),fill_color='#ffffgg').add_to(seoul)
    if getDistanceBetweenPointsNew(37.4971850, 126.927595, location.iloc[i,1], location.iloc[i,2]) < markers :
        markers = getDistanceBetweenPointsNew(37.4971850, 126.927595, location.iloc[i,1], location.iloc[i,2])
        loc_h, loc_v = location.iloc[i,1], location.iloc[i,2]


# Marker / Sejong Univ.
folium.Marker([37.4971850, 126.927595], icon=folium.Icon(popup='Dongjak-gu', color='red', icon='glyphicon glyphicon-home')).add_to(seoul)
folium.Marker([loc_h, loc_v], icon=folium.Icon(popup='test', color='blue', icon='glyphicon glyphicon-home')).add_to(seoul)


seoul
