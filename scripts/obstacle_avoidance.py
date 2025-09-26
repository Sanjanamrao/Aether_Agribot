from scripts.gps_simulation import generate_zigzag_path
import math
import folium

def distance(a,b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def detour_around_obstacles(path_points, obstacles, threshold=0.00005):
    """
    Simple detour: if a path point is within threshold distance to an obstacle,
    replace that segment with a small bypass (move a bit to side, advance, then come back).
    This is a demo algorithm for visualization — replace with A*/RRT for real robots.
    """
    new_path = []
    for p in path_points:
        hit = False
        for obs in obstacles:
            if distance(p, obs) < threshold:
                hit = True
                # detour: shift perpendicular (~add small delta lon), move forward, shift back
                shift = 0.00008
                new_path.append((p[0], p[1] + shift))
                new_path.append((p[0] + 0.00005, p[1] + shift))
                new_path.append((p[0] + 0.00005, p[1]))
                break
        if not hit:
            new_path.append(p)
    return new_path

def run_demo_with_obstacles(start_lat=12.9716, start_lon=77.5946, obstacles=None, rows=8, cols=15):
    if obstacles is None:
        # sample obstacles near the field
        obstacles = [(start_lat + 0.00024, start_lon + 0.0007)]
    base_path = generate_zigzag_path(start_lat, start_lon, rows=rows, cols=cols)
    new_path = detour_around_obstacles(base_path, obstacles)
    return {'base_len': len(base_path), 'new_len': len(new_path), 'base_path': base_path, 'new_path': new_path, 'obstacles': obstacles}



def make_map_with_obstacles(base_path, new_path, obstacles, start_loc, save_path='gps_obstacle_map.html'):
    m = folium.Map(location=start_loc, zoom_start=18)
    folium.PolyLine(base_path, color='gray', weight=2, opacity=0.5).add_to(m)
    folium.PolyLine(new_path, color='blue', weight=3, opacity=0.8).add_to(m)
    for obs in obstacles:
        folium.CircleMarker(location=obs, radius=5, color='red', fill=True, popup="Obstacle").add_to(m)
    folium.Marker(base_path[0], popup="Start").add_to(m)
    folium.Marker(base_path[-1], popup="End").add_to(m)
    m.save(save_path)
    return save_path
