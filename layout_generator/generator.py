import random
import copy
import math
from geometry import Site, Building
from constraints import validate_placement, check_neighbor_mix_rule

class LayoutGenerator:
    def __init__(self, site):
        self.site = site
        
    def generate_random_layout(self, num_attempts=200):
        buildings = []
        for _ in range(num_attempts):
            b = self.site.get_random_building()
            if validate_placement(b, buildings, self.site):
                buildings.append(b)
        return buildings

    def improve_mix(self, buildings, max_attempts=100):
        full_valid, violating_As = check_neighbor_mix_rule(buildings)
        if full_valid:
            return buildings
            
        new_buildings = copy.deepcopy(buildings)
        
        for a in violating_As:
            placed = False
            for _ in range(50):
                angle = random.uniform(0, 6.28)
                dist = random.uniform(20, 55)
                nx = a.x + dist * math.cos(angle)
                ny = a.y + dist * math.sin(angle)
                cand_b = Building(nx, ny, 'B')
                
                if cand_b.poly.distance(a.poly) > 60:
                    continue
                    
                if validate_placement(cand_b, new_buildings, self.site):
                    new_buildings.append(cand_b)
                    placed = True
                    break
        
        return new_buildings

    def generate_population(self, n=10):
        layouts = []
        for i in range(n):
            layout = self.generate_random_layout()
            layout = self.improve_mix(layout)
            layouts.append(layout)
        return layouts
        
    def score_layout(self, buildings):
        score = 0
        score += len(buildings) * 10
        
        valid, violating = check_neighbor_mix_rule(buildings)
        if valid:
            score += 1000
        else:
            score -= len(violating) * 50
            
        area = sum([b.width * b.height for b in buildings])
        score += area * 0.01
        return score
