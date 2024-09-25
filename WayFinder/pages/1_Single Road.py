import streamlit as st
import modules.single_feature as sf

searchFor = st.text_input('Enter the Road Name')
searchArea = st.text_input('Enter the search area', value="Singapore")
start_btn = st.button('Start Query')
    
if start_btn:
    result = sf.single_road_query(searchFor, searchArea)
    st.text_area(label="Way IDs",value=result, height=500)