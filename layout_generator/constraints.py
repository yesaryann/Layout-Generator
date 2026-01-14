from shapely.geometry import box

MIN_DIST_BETWEEN_BUILDINGS = 15.0
SITE_SETBACK = 10.0
NEIGHBOR_RADIUS = 60.0

def validate_placement(building, existing_buildings, site):
    if not site.bounds.contains(building.poly):
        return False
        
    safe_zone = box(SITE_SETBACK, SITE_SETBACK, 
                   site.width - SITE_SETBACK, site.height - SITE_SETBACK)
    if not safe_zone.contains(building.poly):
        return False

    if building.poly.intersects(site.plaza):
        return False

    for other in existing_buildings:
        if building.poly.distance(other.poly) < MIN_DIST_BETWEEN_BUILDINGS:
            return False
            
    return True

def check_neighbor_mix_rule(buildings):
    violating_As = []
    
    tower_As = [b for b in buildings if b.building_type == 'A']
    tower_Bs = [b for b in buildings if b.building_type == 'B']
    
    if not tower_As:
        return True, []
        
    for a in tower_As:
        found_neighbor = False
        for b in tower_Bs:
            if a.poly.distance(b.poly) <= NEIGHBOR_RADIUS:
                found_neighbor = True
                break
        
        if not found_neighbor:
            violating_As.append(a)
            
    return len(violating_As) == 0, violating_As
