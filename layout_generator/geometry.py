from shapely.geometry import box
import random

class Building:
    def __init__(self, x, y, building_type):
        self.x = x
        self.y = y
        self.building_type = building_type
        
        if building_type == 'A':
            self.width = 30
            self.height = 20
        elif building_type == 'B':
            self.width = 20
            self.height = 20
        else:
            raise ValueError(f"Unknown building type: {building_type}")
            
        self.poly = box(x, y, x + self.width, y + self.height)

    def __repr__(self):
        return f"Building({self.building_type}, {self.x:.1f}, {self.y:.1f})"

class Site:
    def __init__(self, width=200, height=140):
        self.width = width
        self.height = height
        self.bounds = box(0, 0, width, height)
        self.plaza = box(80, 50, 120, 90)

    def get_random_building(self):
        b_type = random.choice(['A', 'B'])
        if b_type == 'A':
            w, h = 30, 20
        else:
            w, h = 20, 20
            
        x = random.uniform(0, self.width - w)
        y = random.uniform(0, self.height - h)
        return Building(x, y, b_type)
