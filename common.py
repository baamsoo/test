import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
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

# PM10에 따른 color 변화
def color_select(x):
    if x >= 45:
        return 'red'
    elif x >= 40:
        return 'yellow'
    else:
        return 'blue'

def get_sales():
    data = pd.read_csv("https://raw.githubusercontent.com/baamsoo/test/main/Measurement_summary.csv")
    data.dropna(inplace=True)
    return data

def page_config():
    st.set_page_config(
        page_title="test",
        page_icon="🏥",
    )
