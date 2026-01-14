import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from constraints import check_neighbor_mix_rule, SITE_SETBACK

def render_layout(site, buildings, output_path=None, title="Layout"):
    fig, ax = plt.subplots(figsize=(10, 7))
    
    site_rect = Rectangle((0,0), site.width, site.height, 
                          edgecolor='black', facecolor='#f0f0f0', lw=2)
    ax.add_patch(site_rect)
    
    setback_rect = Rectangle((SITE_SETBACK, SITE_SETBACK), 
                             site.width - 2*SITE_SETBACK, site.height - 2*SITE_SETBACK,
                             edgecolor='gray', facecolor='none', linestyle='--')
    ax.add_patch(setback_rect)
    
    px, py = site.plaza.bounds[0], site.plaza.bounds[1]
    pw = site.plaza.bounds[2] - px
    ph = site.plaza.bounds[3] - py
    plaza_patch = Rectangle((px, py), pw, ph, 
                            edgecolor='green', facecolor='#ccffcc', hatch='//')
    ax.add_patch(plaza_patch)
    
    layout_valid, violating_As = check_neighbor_mix_rule(buildings)
    
    for b in buildings:
        color = 'blue' if b.building_type == 'A' else 'orange'
        
        if b in violating_As:
            edge_color = 'red'
            line_width = 3
        else:
            edge_color = 'black'
            line_width = 1
            
        rect = Rectangle((b.x, b.y), b.width, b.height, 
                         facecolor=color, edgecolor=edge_color, lw=line_width, alpha=0.8)
        ax.add_patch(rect)
        
        cx = b.x + b.width/2
        cy = b.y + b.height/2
        ax.text(cx, cy, b.building_type, ha='center', va='center', color='white', weight='bold')
        
    ax.set_xlim(-10, site.width + 10)
    ax.set_ylim(-10, site.height + 10)
    ax.set_aspect('equal')
    ax.set_title(title)
    
    if output_path:
        plt.savefig(output_path, bbox_inches='tight')
    
    plt.close(fig) 
