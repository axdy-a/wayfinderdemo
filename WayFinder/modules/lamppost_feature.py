import json
import modules.overpassAPI as api
import modules.bounding_box as bbox
import modules.helper as hlp
import modules.between_feature as bwt




def lamp_post_query(lamp_post, lamp_post_road, searchFor, condition_roads ,searchArea="Singapore"):
    """
    This function is used to find way ids of a road, between a lamp post and a condition road.
    This means we assume the lamp post is on the condition road. There should be only 1 condition road.
    
    Params:
    - lamp_post: The lamp post number to search for.
    - searchFor: The road to search for.
    - condition_roads: The road to search for lamp post.
    - searchArea: The area to search for. Default is Singapore.
    
    Returns:

        
    """
    
    if searchFor and condition_roads and searchArea and lamp_post and lamp_post_road:
        pass
    else:
        return "Missing Inputs!"
    
    
    condition_nodes     = hlp.get_nodes(condition_roads, searchArea)
    search_for_nodes    = hlp.get_nodes(searchFor, searchArea)
    lamppost_road_nodes = hlp.get_nodes(lamp_post_road, searchArea)
    intersections       = hlp.find_intersection(search_for_nodes, condition_nodes)
    
    if not intersections:
        # should attempt to find highway nodes (brute force)     
        return "No intersections found with condition road"
    
    sorted_search_nodes = hlp.sort_nodes_by_lat_lng(lamppost_road_nodes)
    
    lamppost_road_first_node = [[sorted_search_nodes[0][1], sorted_search_nodes[0][2]]]
    lamppost_road_last_node  = [[sorted_search_nodes[-1][1], sorted_search_nodes[-1][2]]]
    
    #debug
    print(lamppost_road_first_node, lamppost_road_last_node)
    
    v1, v2, v3, v4 = bbox.construct_by_two_lists(lamppost_road_first_node, lamppost_road_last_node)
    bounding_box   = bbox.shrink_or_expand_percentage([v1, v2, v3, v4], 50, False)
    
    #debug
    print(",".join([bounding_box[0],bounding_box[1]]))
    print(",".join([bounding_box[2],bounding_box[3]]))
    
    lamppost_coordinates = get_lamppost_coordinates(lamp_post)

    # Check if any coordinates in lamppost_coordinates is within the bbox
    results = bbox.check_if_inside_bbox(lamppost_coordinates, bounding_box)
    
    if not results:
        return("No lamp post found in the search area")
    
    way_id_results = []
    for result in results:

        coords = ",".join(result)
        
        test = api.overpass_query(api.query_selector("lamp_post",lamp_post_road, searchArea, coords))

        if len(test['elements']) > 0:
            print("Found Lamp Post Road. Using this as the condition road")
            way_id_results = bwt.between_way_query(searchFor, searchArea, intersections, [result])
            
            
        if way_id_results:
            ways = ",".join(way_id_results)
            return(f"Way IDs found:\n{ways} \n\nLat Long of Lamp Post: {coords}")

    return "No lamp post found in the search area"




def get_lamppost_coordinates(lamp_post):
    '''
    Function to get the coordinates of all matching lamp posts
    
    Params:
        lamp_post: str - The lamp post number to search for
        latlng_list: list - List of latlng coordinates
    
    '''
    coordinates = []
    
    with open('data/extracted_data_complied.json', 'r') as f:
        extracted_data = json.load(f)
        
        for lamppost in extracted_data:
            if lamppost["LAMPPOST_NUM"] == lamp_post:
                coordinates.append(lamppost["LatLng"].split(","))
    
    return coordinates