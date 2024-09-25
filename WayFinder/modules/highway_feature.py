import modules.between_feature as bf


def highway_query(condition_nodes, intersections, searchFor, searchArea="Singapore"):
    '''
    This function is used to find the roads (ways) that are between a highway/flyover and intersected road.
    
    Params:
        condition_nodes: list - The list of nodes from the condition road
        intersections: list - The list of nodes that intersect with the search road
        searchFor: str - The road to search for
        searchArea: str - The area to search in
    
    '''
    
    highway_nodes = find_highway_nodes(condition_nodes, intersections)
    
    if not highway_nodes:
        return "Unable to find highway nodes!"
    
    highway_list = [[highway_nodes[0][1], highway_nodes[0][2]]]
    result1 = bf.between_way_query(searchFor, searchArea, intersections, highway_list)
        
    highway_list = [[highway_nodes[-1][1], highway_nodes[-1][2]]]
    result2 = bf.between_way_query(searchFor, searchArea, intersections, highway_list)
        
    #combine result and result2, unique values
    return list(set(result1) | set(result2))




def find_highway_nodes(condition_nodes, intersections):
    """
    Based on known intersection, find the 2 closest condition nodes on the opposite side to the intersection.
    Thus, forming a side of the bounding box where it is a highway/flyover.
    
    Params:
        condition: list - List of nodes from the condition road
        intersections: list - List of nodes that intersect with the search road

    """
    
    min_diff_lat = []
    
    for nodes in condition_nodes:
        # Find the difference between the first intersection and all the condition node
        diff = intersections[0][0] - nodes[1]
        
        # Convert to positive value
        if diff < 0:
            diff *= -1
        
        # Append the difference and the node id
        min_diff_lat.append([diff,nodes[0]])
    
    # Sort the list based on the difference   
    min_diff_lat.sort(key=lambda x: x[0])

    # Selects top two closest nodes
    target_ids = {min_diff_lat[0][1],min_diff_lat[1][1]}
    
    result = []
    
    # Find the nodes with the target ids
    for node in condition_nodes:
        if node[0] in target_ids:
            result.append(node)
    
    if result[1]:
        return [result[0],result[1]]