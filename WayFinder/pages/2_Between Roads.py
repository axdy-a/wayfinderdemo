import streamlit as st
import modules.between_feature as bwt

st.markdown("""
### Between Roads
Query for all way ids belonging to X road, between Y road and Z road.
- Road name (X road)
- Condition Roads (Y road & Z road)
- Search area (Country name)
<br>
""", unsafe_allow_html=True)

searchFor = st.text_input('Enter the Road Name')
condition1 = st.text_input('Enter the first condition road')
condition2  = st.text_input('Enter the second condition road')
options = ["Singapore", "Malaysia", "Indonesia", "Cambodia", "Myanmar", "Philippines", "Thailand", "Vietnam"]
searchArea = st.selectbox("Choose a country:", options)
start_btn = st.button('Start Query')

if start_btn:
    result = bwt.between_query(searchFor, [condition1, condition2], searchArea)
    result = ",".join(result)
    st.write(result)