import streamlit as st
import pandas as pd
import numpy as n
from numpy import sin, cos, arccos, pi, round

@st.cache_data

def get_sales():
    data = pd.read_csv("https://raw.githubusercontent.com/baamsoo/test/main/Measurement_summary.csv")
    data.dropna(inplace=True)
    return data

def page_config():
    st.set_page_config(
        page_title="test",
        page_icon="🏥",
    )
