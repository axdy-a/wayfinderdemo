import streamlit as st
import modules.between_feature as bwt


searchFor = st.text_input('Enter the Road Name')
condition1 = st.text_input('Enter the first condition road')
condition2  = st.text_input('Enter the second condition road')
searchArea = st.text_input('Enter the search area', value="Singapore")
start_btn = st.button('Start Query')

if start_btn:
    result = bwt.between_query(searchFor, [condition1, condition2], searchArea)
    result = ",".join(result)
    st.write(result)