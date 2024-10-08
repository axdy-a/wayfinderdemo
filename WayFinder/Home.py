import streamlit as st

st.markdown("""
# WayFinder Demo   

Welcome to the WayFinder Demo!

From this app, you can select a way ID function to approximately find the road way ID information.\\
This is helpful with road closures that come via text format (emails / letters / notices).\\
**All inputs have to be in long form or in OpenStreetMap Standards. (Wrong: ~~Ave~~ | Correct: Avenue)**

**NOTE:** Program is still in the testing phase! Do contact us at #sg-mapops-feedback for questions or issues.
Expect inconsistencies with roads that curve a lot. (Still exploring solutions)

Made by SG MapOps Team.

## Functions:

### Single Road
Query for all way ids belonging to a specific road.
- Road name (Full name)
- Search area (Country name)

### Between Roads
Query for all way ids belonging to X road, between Y road and Z road.
- Road name (X road)
- Condition Roads (Y road & Z road)
- Search area (Country name)

### Lamp Post Query (Singapore Only)
Query for all way ids, starting from a lamp post (number), that is on X road to the node where X road intersect Y road.
- Lamp post number
- Road name that lamp post is on
- Road name (X road)
- Condition Road (Y road)


""", unsafe_allow_html=True)

# select = st.selectbox('Select a Way ID function', ["None","Single Road","Between Roads","Lamp Post Condition"])

# if select == "Single Road":
#     searchFor = st.text_input('Enter the Road Name')
#     searchArea = st.text_input('Enter the search area', value="Singapore")
#     start_btn = st.button('Start Query')
    
#     if start_btn:
#         result = sf.single_road_query(searchFor, searchArea)
#         st.text_area(label="Way IDs",value=result, height=500)

# elif select == "Between Roads":
#     searchFor = st.text_input('Enter the Road Name')
#     condition1 = st.text_input('Enter the first condition road')
#     condition2  = st.text_input('Enter the second condition road')
#     searchArea = st.text_input('Enter the search area', value="Singapore")
#     start_btn = st.button('Start Query')
    
#     if start_btn:
#         result = bwt.between_query(searchFor, [condition1, condition2], searchArea)
#         st.write(result)

# elif select == "Lamp Post Condition":
#     lamp_post = st.text_input('Enter the lamp post number')
#     lamp_post_road = st.text_input('Enter the road name of the lamp post')
#     searchFor = st.text_input('Enter the road name to search for')
#     condition1 = st.text_input('Enter the condition road')
#     searchArea = st.text_input('Enter the search area', value="Singapore")
    
#     start_btn = st.button('Start Query')
    
#     if start_btn:
#         result = lpf.lamp_post_query(lamp_post, lamp_post_road, searchFor, condition1, searchArea)
#         st.write(result)
#         result_array = result.split("\n")

#         pattern = r"(\d+\.\d+),(\d+\.\d+)"
#         match = re.search(pattern, result_array[-1])

#         if match:
#             lat = match.group(1)  # The first group (1.36492618097596)
#             lon = match.group(2)  # The second group (103.843396643166)
#         else:
#             lat,lon = None,None
            
#         if lat and lon:
#             lat,lon = float(lat),float(lon)
#             m = folium.Map(location=[lat, lon], zoom_start=16)
#             folium.Marker(
#                 [lat, lon], popup="Lamp Post", tooltip="Lamp Post"
#             ).add_to(m)

#             # call to render Folium map in Streamlit, but don't get any data back
#             # from the map (so that it won't rerun the app when the user interacts)
#             st_folium(m, width=725, returned_objects=[])
                    
