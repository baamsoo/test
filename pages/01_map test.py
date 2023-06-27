import streamlit as st
from streamlit_folium import st_folium
import folium
import common

common.page_config()

st.title("Dot Map Visualization")

data = common.get_sales()

# 지도 초기화
map_korea = folium.Map(location=[36.5, 127.5], zoom_start=7)

# 데이터 시각화
for idx, row in data.iterrows():
    lat, lon = row['latitude'], row['longitude']
    
    # CircleMarker를 사용하여 도트맵 표현
    folium.CircleMarker(
        location=[lat, lon],
        radius=1,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6
    ).add_to(map_korea)

# https://github.com/randyzwitch/streamlit-folium/blob/master/examples/streamlit_app.py
# 지도 출력
st_folium(map_korea)
