import modules.overpassAPI as api


def getLength(wayids):
    
    try:
        waylist = str(wayids).strip()
        data = api.overpass_query(api.ukm_length_query(waylist)) 
        return f"{float(data["elements"][-1]["tags"]["length"])/1000:.4f}"
    
    except:
        return "Error: Check your way id input"

