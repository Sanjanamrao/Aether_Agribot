import folium
import math
import os

# Use lat/lon starting point and small steps to simulate a field
def generate_zigzag_path(start_lat, start_lon, rows=10, cols=20, step_lat=0.00012, step_lon=0.00014):
    """
    Generate boustrophedon (zig-zag) path in lat-lon coordinates.
    rows = number of rows in Y direction
    cols = number of columns in X direction
    """
    points = []
    lat = start_lat
    lon = start_lon
    direction = 1
    for r in range(rows):
        row_points = []
        for c in range(cols):
            row_points.append((lat, lon))
            lon += direction * step_lon
        # after finishing a row, go up one step in lat, reverse direction
        points.extend(row_points if direction==1 else list(reversed(row_points)))
        direction *= -1
        lat += step_lat
    return points

def make_folium_map(points, start_loc=None, save_path='gps_path.html'):
    if start_loc is None:
        start_loc = points[0]
    m = folium.Map(location=start_loc, zoom_start=18)
    folium.PolyLine(points, color='blue', weight=3, opacity=0.8).add_to(m)
    folium.Marker(points[0], popup="Start").add_to(m)
    folium.Marker(points[-1], popup="End").add_to(m)
    m.save(save_path)
    return save_path

# Demo function for Streamlit
def run_demo(start_lat=12.9716, start_lon=77.5946, rows=8, cols=15):
    points = generate_zigzag_path(start_lat, start_lon, rows=rows, cols=cols)
    html_path = make_folium_map(points, start_loc=(start_lat, start_lon), save_path='gps_path.html')
    return {'html': html_path, 'points_count': len(points)}
