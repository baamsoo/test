import streamlit as st
from streamlit_folium import st_folium
import folium
import common

common.page_config()

st.title("Dot Map Visualization")

data = common.get_sales()

# 위도 경도 DataFrame
location = df.groupby('Station code')['PM10'].agg([np.mean])
location['Latitude'] = df['Latitude'].unique()
location['Longitude'] = df['Longitude'].unique()
location.head()

# Map
seoul = folium.Map(location=[37.55138077230307, 126.98712254969668], zoom_start=12)

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


# https://github.com/randyzwitch/streamlit-folium/blob/master/examples/streamlit_app.py
# 지도 출력
st_folium(seoul)
