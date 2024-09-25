import modules.overpassAPI as api

def single_road_query(searchFor, searchArea="Singapore"):
    """
    This function is used to find the way ids of a single road
    Params:
        searchFor: str - The road to search for
        searchArea: str - The area to search in
        
    """
    
    if searchFor and searchArea:
        pass
    else:
        return "Missing Inputs!"
    
    
    type = "road"
    id_type = "way"
    result = api.get_element_list(id_type, api.overpass_query(api.query_selector(type, searchFor, searchArea)))
    
    result = ",".join(result)
    
    return (f"Way IDs for {searchFor} (Copy and Paste):\n{result.strip()}")