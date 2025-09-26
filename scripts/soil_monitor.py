import numpy as np
import pandas as pd
import time

def simulate_sensor_series(n_points=100, seed=42):
    np.random.seed(seed)
    # simulate soil moisture, temperature, battery level as random walk
    moisture = np.clip(50 + np.cumsum(np.random.randn(n_points) * 0.5), 10, 100)
    temp = np.clip(25 + np.cumsum(np.random.randn(n_points) * 0.1), -5, 50)
    battery = np.clip(100 - np.cumsum(np.abs(np.random.randn(n_points))*0.2), 0, 100)
    times = pd.date_range(end=pd.Timestamp.now(), periods=n_points).astype(str)
    df = pd.DataFrame({'time': times, 'soil_moisture': moisture, 'temperature': temp, 'battery': battery})
    return df

def run_demo():
    df = simulate_sensor_series()
    # summary
    summary = {
        'moisture_latest': float(df['soil_moisture'].iloc[-1]),
        'temp_latest': float(df['temperature'].iloc[-1]),
        'battery_latest': float(df['battery'].iloc[-1]),
        'dataframe': df
    }
    return summary
