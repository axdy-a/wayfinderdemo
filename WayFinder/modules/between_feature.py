import modules.overpassAPI as api
import modules.bounding_box as bbox
import modules.helper as hlp
import modules.highway_feature as hwf



def between_query(searchFor, condition_roads, searchArea="Singapore"):
    '''
    This function is used to find the roads (ways) that are between two roads.
    
    Params:
        searchFor: str - The road to search for
        condition_roads: list - The list of roads to search between
        searchArea: str - The area to search in
        
    '''
    if not searchFor and not condition_roads and not searchArea:
        return "Missing Inputs!"
    
    search_for_nodes  = hlp.get_nodes(searchFor, searchArea)
    condition_1_nodes = hlp.get_nodes(condition_roads[0], searchArea)
    condition_2_nodes = hlp.get_nodes(condition_roads[1], searchArea)
    intersections_1, intersections_2 = hlp.find_intersection(search_for_nodes, condition_1_nodes, condition_2_nodes)
    
    # Found intersection with both condition roads
    if intersections_1 and intersections_2:
        result = between_way_query(searchFor, searchArea, intersections_1, intersections_2)
    
    # Found intersection with only one condition road
    elif not intersections_1:
        print("Unable to find intersection with search road for condition 1. Checking for highway nodes...")
        result = hwf.highway_query(condition_1_nodes, intersections_2, searchFor, searchArea)
        
    # Found intersection with only one condition road
    elif not intersections_2:
        print("Unable to find intersection with search road for condition 2. Checking for highway nodes...")
        result = hwf.highway_query(condition_2_nodes, intersections_1, searchFor, searchArea)
    
    # TODO: Found no intersection but one highway intersection
    
    # TODO: Found no intersection but one condition intersection
    
    if result: 
        return result
    else:
        return None




def between_way_query(searchFor, searchArea, c1_list, c2_list):
    '''
    This function is used to find the roads (ways) that are between two roads.
    
    Params:
        searchFor: str - The road to search for
        searchArea: str - The area to search in
        c1_list: list - The list of coordinates of the first road
        c2_list: list - The list of coordinates of the second road
    
    '''
    type = "between"
    id_type = "way"
    
    v1, v2, v3, v4  = bbox.construct_by_two_lists(c1_list, c2_list)
    shrinked        = ",".join(bbox.shrink_or_expand_percentage([v1, v2, v3, v4], 0.5))
    result          = api.get_element_list(id_type, api.overpass_query(api.query_selector(type, searchFor, searchArea, shrinked)))
    return result
