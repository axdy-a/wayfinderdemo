import re
import folium
import streamlit as st
from streamlit_folium import st_folium
import modules.ukmlength as ukm

st.markdown("""
### UKM Length Calculator
Insert all way ids
<br>
""", unsafe_allow_html=True)

wayids = st.text_input('Enter way ids (Separate by comma):')

start_btn = st.button('Get Length')

if start_btn:
    st.write(ukm.getLength(wayids))