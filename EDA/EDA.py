import pandas as pd
import numpy as np
import os

from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import geodatasets

import matplotlib.pyplot as plt


df = pd.read_csv('../data_with_state.csv')
# Set the coordinate reference system (CRS)
geo_df.crs = 'EPSG:4326'  # WGS84

world = gpd.read_file(geodatasets.data.naturalearth.land['url'])
country_map = gpd.read_file('india_ds.shp')
# Create geometry from latitude and longitude
# week1

def plot_chart_with_metric(n=1):
    df1 = df.loc[df.week_no == n, ]
    geometry = [Point(xy) for xy in zip(df1['lon'], df1['lat'])]
    geo_df = gpd.GeoDataFrame(df1, geometry=geometry)

    # Filter the DataFrame
    filtered_gdf = geo_df[geo_df.within(country_map.unary_union)]

    # Plot the world map
    fig, ax = plt.subplots(figsize=(10, 10))
    filtered_gdf.boundary.plot(ax=ax, linewidth=1)

    # Plot the GeoDataFrame with a colormap based on the metric
    # You can choose the 'cmap' as per your preference
    filtered_gdf.plot(column='gws_inst', ax=ax, legend=True, 
                cmap='Greens', markersize=100, alpha=0.7)

    # Add a title
    plt.title('Groundwater')
    plt.show()

plot_chart_with_metric(1) #2nd Jan 2023
plot_chart_with_metric(53) #1st Jan 2024
plot_chart_with_metric(71) #6th May 2024