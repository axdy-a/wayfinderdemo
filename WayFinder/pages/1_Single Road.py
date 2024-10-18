import streamlit as st
import modules.single_feature as sf

st.markdown("""
### Single Road
Query for all way ids belonging to a specific road.
- Road name (Full name)
- Search area (Country name)
<br>
""", unsafe_allow_html=True)


searchFor = st.text_input('Enter the Road Name')

options = ["Singapore", "Malaysia", "Indonesia", "Cambodia", "Myanmar", "Philippines", "Thailand", "Vietnam"]
searchArea = st.selectbox("Choose a country:", options)

start_btn = st.button('Start Query')
    
if start_btn:
    result = sf.single_road_query(searchFor, searchArea)
    st.text_area(label="Way IDs",value=result, height=500)