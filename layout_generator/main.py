import os
from geometry import Site
from generator import LayoutGenerator
from visualizer import render_layout
from constraints import check_neighbor_mix_rule

def main():
    site = Site()
    gen = LayoutGenerator(site)
    
    population_size = 50
    population = gen.generate_population(population_size)
    
    scored_pop = []
    for layout in population:
        score = gen.score_layout(layout)
        scored_pop.append((score, layout))
        
    scored_pop.sort(key=lambda x: x[0], reverse=True)
    
    output_dir = "output_layouts"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for i in range(min(5, len(scored_pop))):
        score, buildings = scored_pop[i]
        valid_mix, _ = check_neighbor_mix_rule(buildings)
        
        count_a = sum(1 for b in buildings if b.building_type == 'A')
        count_b = sum(1 for b in buildings if b.building_type == 'B')
        total_area = sum(b.width * b.height for b in buildings)
        
        print(f"Rank {i+1}: Score={score:.1f}, A={count_a}, B={count_b}, Area={total_area}")
        
        filename = os.path.join(output_dir, f"layout_rank_{i+1}.png")
        title = f"Rank {i+1} | Score: {score:.0f}"
        render_layout(site, buildings, output_path=filename, title=title)

if __name__ == "__main__":
    main()
