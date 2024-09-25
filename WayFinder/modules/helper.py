import modules.overpassAPI as api

def sort_nodes_by_lat_lng(nodes):
    """
    Sorts the nodes by latitude and longitude
    
    Params:
        nodes: list - List of nodes to be sorted
        
    Returns:
        list - List of sorted nodes
    """
    
    sorted_nodes = sorted(nodes, key=lambda x: (x[1], x[2]))
    
    return sorted_nodes 




def find_intersection(sv, c1, c2=[]) -> list:
    """
    Function to find the intersection between the search road and the condition roads
    
    Params:
        sv: list - List of nodes from the search road
        c1: list - List of nodes from condition 1 road
        c2: list - List of nodes from condition 2 road
        
        
    Returns:
        list - List of nodes that intersect with the search road
        
    """
    def process_nodes(nodes, condition_nodes, results, condition_message):
        '''
        Function to process nodes and find the intersection
        
        Params:
            nodes: list - List of nodes to be processed
            condition_nodes: list - List of nodes from the condition road
            results: list - List of nodes that intersect with the search road
            condition_message: str - Message to be printed when the intersection is found
            
        Returns:
            list - List of nodes that intersect with the search
        
        '''
        for node in nodes:
            
            for c_node in condition_nodes:
                
                if node == c_node:
                    
                    n1, n2 = float(node[1]), float(node[2])
                    results.append([n1, n2])
                    print(condition_message)

    c1_results = []
    c2_results = []

    process_nodes(sv, c1, c1_results, "Found intersection with condition 1 road")
    process_nodes(sv, c2, c2_results, "Found intersection with condition 2 road")

    if not c2:
        return c1_results
    else:
        return c1_results, c2_results




def get_nodes(road, searchArea="Singapore", query_type="road", id_type="node"):
        return api.get_element_list(id_type, api.overpass_query(api.query_selector(query_type, road, searchArea)))