import math

def construct_by_two_coordinates(lat1, lng1, lat2, lng2):
    """
    Constructs a bounding box given two latitude and longitude points,
    by taking the minimum and maximum values of the coordinates.

    Params:
        lat1, lng1: Latitude and longitude of the first point.
        lat2, lng2: Latitude and longitude of the second point.

    Returns:
        tuple: Coordinates in str of the bounding box (min_lat, min_lng, max_lat, max_lng).
    """
    lat1 = float(lat1)
    lng1 = float(lng1)
    lat2 = float(lat2)
    lng2 = float(lng2)
    
    min_lat = min(lat1, lat2)
    max_lat = max(lat1, lat2)
    min_lng = min(lng1, lng2)
    max_lng = max(lng1, lng2)

    return min_lat, min_lng, max_lat, max_lng




def find_min_max_coordinates(coord_list):
    """
    Finds the minimum and maximum latitude and longitude from a list of coordinates.

    Params:
        coord_list: list - List of coordinates.

    Returns:
        tuple: (min_lat, min_lng, max_lat, max_lng)
        
    """
    if len(coord_list) == 1:
        lat = float(coord_list[0][0])
        lng = float(coord_list[0][1])
        return lat, lng, lat, lng

    latitudes = [float(coord[0]) for coord in coord_list]
    longitudes = [float(coord[1]) for coord in coord_list]

    return min(latitudes), min(longitudes), max(latitudes), max(longitudes)




def construct_by_two_lists(c1_list, c2_list):
    """
    Constructs a bounding box given two lists of coordinates.
    
    Params:
        c1_list: list - List of coordinates from the first road.
        c2_list: list - List of coordinates from the second road.
        
    Returns:
        tuple: Coordinates in float of the bounding box (min_lat, min_lng, max_lat, max_lng)
        
    """
    c1_min_lat, c1_min_lng, c1_max_lat, c1_max_lng = find_min_max_coordinates(c1_list)
    c2_min_lat, c2_min_lng, c2_max_lat, c2_max_lng = find_min_max_coordinates(c2_list)

    min_lat = min(c1_min_lat, c2_min_lat)
    min_lng = min(c1_min_lng, c2_min_lng)
    max_lat = max(c1_max_lat, c2_max_lat)
    max_lng = max(c1_max_lng, c2_max_lng)

    return min_lat, min_lng, max_lat, max_lng




def shrink_or_expand_percentage(bbox, percentage, shrink=True):
    '''
    Function to shrink or expand a bounding box by a specified percentage.
    
    Params:
        bbox: list - Bounding box coordinates [min_lat, min_lng, max_lat, max_lng].
        percentage: float - Percentage by which to shrink or expand the bounding box.
        shrink: bool - If True, the bounding box will be shrunk, otherwise it will be expanded.
        
    Returns:
        list: Coordinates in str of the shrinked or expanded bounding box [min_lat, min_lng, max_lat, max_lng].
        
    '''
    
    min_lat, min_lng, max_lat, max_lng = bbox
    
    lat_diff = max_lat - min_lat
    lng_diff = max_lng - min_lng
    
    percent_change_lat = lat_diff * (percentage / 100)
    percent_change_lng = lng_diff * (percentage / 100)
    
    if shrink == True:
        new_min_lat = str(min_lat + percent_change_lat)
        new_min_lng = str(min_lng + percent_change_lng)
        new_max_lat = str(max_lat - percent_change_lat)
        new_max_lng = str(max_lng - percent_change_lng)
    
    else: #expand
        
        new_min_lat = str(min_lat - percent_change_lat)
        new_min_lng = str(min_lng - percent_change_lng)
        new_max_lat = str(max_lat + percent_change_lat)
        new_max_lng = str(max_lng + percent_change_lng)
        
    return [new_min_lat, new_min_lng, new_max_lat, new_max_lng]




# Brute force method
def create_by_single_latlng(lat, lng, expansion_factor=0.05, distance_km=0.5):
    '''
    Function to create a bounding box given a single latitude and longitude point.
    
    Params:
        lat: float - Latitude of the point.
        lng: float - Longitude of the point.
        expansion_factor: float - Factor by which to expand the bounding box.
        distance_km: float - Distance in km to expand the bounding box.
        
    '''
    DEGREE_TO_KM = 111.32  # Approximate km per degree latitude at the equator

    # Calculate degrees per km
    lat_degree_per_km = 1 / DEGREE_TO_KM
    lon_degree_per_km = 1 / (DEGREE_TO_KM * math.cos(math.radians(lat)))

    # Calculate the distance in degrees
    lat_offset_deg = distance_km * lat_degree_per_km
    lon_offset_deg = distance_km * lon_degree_per_km

    # Apply the expansion factor
    lat_north = lat + lat_offset_deg * expansion_factor
    lat_south = lat - lat_offset_deg * expansion_factor
    lng_east  = lng + lon_offset_deg * expansion_factor
    lng_west  = lng - lon_offset_deg * expansion_factor

    # Return the bounding box in the format min_lat, min_lon, max_lat, max_lon
    return [lat_south, lng_west, lat_north, lng_east]




def check_if_inside_bbox(latlng_list, bbox):
    """
    Function to check if a list of latitude and longitude points are within a bounding box.
    
    Params:
        latlng_list: list - List of latitude and longitude points.
        bbox: list - Bounding box coordinates [min_lat, min_lng, max_lat, max_lng].
        
    Returns:
        list: List of latitude and longitude points that are within the bounding box.
        
    """
    
    min_lat, min_lng, max_lat, max_lng = bbox

    result = []
    
    for latlng in latlng_list:

        lat, lng = float(latlng[0]), float(latlng[1])

        if float(min_lat) <= lat <= float(max_lat) and float(min_lng) <= lng <= float(max_lng):
            result.append(latlng)
    
    return result if result else None
