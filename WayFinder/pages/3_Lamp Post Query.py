import re
import folium
import streamlit as st
from streamlit_folium import st_folium
import modules.lamppost_feature as lpf

st.markdown("""
### Lamp Post Query (Singapore Only)
Query for all way ids, starting from a lamp post (number), that is on X road to the node where X road intersect Y road.
- Lamp post number
- Road name that lamp post is on
- Road name (X road)
- Condition Road (Y road)
<br>
""", unsafe_allow_html=True)

lamp_post = st.text_input('Enter the lamp post number')
lamp_post_road = st.text_input('Enter the road name of the lamp post')
searchFor = st.text_input('Enter the road name to search for')
condition1 = st.text_input('Enter the condition road')
options = ["Singapore", "Malaysia", "Indonesia", "Cambodia", "Myanmar", "Philippines", "Thailand", "Vietnam"]
searchArea = st.selectbox("Choose a country:", options)

start_btn = st.button('Start Query')

if start_btn:
    result = lpf.lamp_post_query(lamp_post, lamp_post_road, searchFor, condition1, searchArea)
    st.write(result)
    result_array = result.split("\n")

    pattern = r"(\d+\.\d+),(\d+\.\d+)"
    match = re.search(pattern, result_array[-1])

    if match:
        lat = match.group(1)  # The first group (1.36492618097596)
        lon = match.group(2)  # The second group (103.843396643166)
    else:
        lat,lon = None,None
        
    if lat and lon:
        lat,lon = float(lat),float(lon)
        m = folium.Map(location=[lat, lon], zoom_start=16)
        folium.Marker(
            [lat, lon], popup="Lamp Post", tooltip="Lamp Post"
        ).add_to(m)

        # call to render Folium map in Streamlit, but don't get any data back
        # from the map (so that it won't rerun the app when the user interacts)
        st_folium(m, width=725, returned_objects=[])