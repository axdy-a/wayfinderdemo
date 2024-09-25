import json
import requests


def overpass_query(query) -> json:
    """
    Function to execute Overpass API query
    
    Params:
        query: str - Overpass query to be executed
        
    Returns:
        json - JSON response from Overpass API
        
    """
    
    overpass_url = "http://overpass-api.de/api/interpreter"
    
    response = requests.get(overpass_url, params={'data': query})
    
    try:
        
        data = response.json()
        
    except ValueError as e:
        
        print(f"Error processing JSON response: {e}")
        return None
        
    return data




def query_selector(type, road, searchArea="Singapore", bbox="", around=50) -> str:
    """
    Function to generate Overpass API query based on type
    
    Params:
        type: str - Type of query to be executed
        road: str - Road name to be queried
        searchArea: str - Area to be searched
        bbox: str - Bounding box for the query
        
    Returns:
        str - Overpass API query
    
    """
    
    
    if type == "road":
        overpass_query = (  
                f"[out:json];\n"
                f"area[name=\"{searchArea}\"]->.searchArea;\n"
                f"way[name=\"{road}\"](area.searchArea);\n"
                f"(._;>;);\n"
                f"out body;")
        
    
    elif type == "between":
        overpass_query = (  
                f"[out:json];\n"
                f"way[name=\"{road}\"]({bbox});\n"
                f"(._;>;);\n"
                f"out body;")
    
    
    elif type == "lamp_post":
        overpass_query = (  
                f"[out:json];\n"
                f"node(around:{around},{bbox});\n"
                f"way(bn)[highway][name=\"{road}\"];\n"
                f"out body;")
    
    
    return overpass_query




def get_element_list(type, data) -> list:
    """
    Function to extract elements from Overpass API response
    
    Params:
        type: str - Type of element to be extracted
        data: json - Overpass API response
        
    Returns:
        list - List of elements extracted from the response
        
    """
    result = []
    
    for element in data['elements']:
        
        if element['type'] == 'node' and type == "node":
            result.append([element['id'],element['lat'],element['lon']])
        
        elif element['type'] == 'way' and type == "way":
            result.append(str(element['id']))
                         
    return result