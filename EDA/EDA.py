import pandas as pd
import numpy as np
import os

from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import geodatasets

import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/ADITHI/Desktop/nasa/gws/NASA_Hackathon_2024_Meteoric_Minds/data_with_state.csv')
# Set the coordinate reference system (CRS)
  # WGS84

world = gpd.read_file(geodatasets.data.naturalearth.land['url'])
country_map = gpd.read_file('C:/Users/ADITHI/Desktop/nasa/gws/NASA_Hackathon_2024_Meteoric_Minds/EDA/india_ds.shp')
# Create geometry from latitude and longitude
# week1

def plot_chart_with_metric(n=1, plot_feature = 'gws_inst', plot_color = 'Greens'):
    df1 = df.loc[df.week_no == n, ]
    geometry = [Point(xy) for xy in zip(df1['lon'], df1['lat'])]
    geo_df = gpd.GeoDataFrame(df1, geometry=geometry)
    geo_df.crs = 'EPSG:4326'
    # Filter the DataFrame
    filtered_gdf = geo_df[geo_df.within(country_map.unary_union)]

    # Plot the world map
    fig, ax = plt.subplots(figsize=(10, 10))
    # filtered_gdf.boundary.plot(ax=ax, linewidth=1)

    # Plot the GeoDataFrame with a colormap based on the metric
    # You can choose the 'cmap' as per your preference
    filtered_gdf.plot(column=plot_feature, ax=ax, legend=True, 
                cmap=plot_color, markersize=100, alpha=0.7)

    # Add a title
    plt.title('Groundwater')
    plt.show()

plot_chart_with_metric(1) #2nd Jan 2023
plot_chart_with_metric(53) #1st Jan 2024
plot_chart_with_metric(71) #6th May 2024

plot_chart_with_metric(1, 'rtzsm_inst', plot_color = 'Reds') #2nd Jan 2023
plot_chart_with_metric(53, 'rtzsm_inst', plot_color = 'Reds') #1st Jan 2024
plot_chart_with_metric(71, 'rtzsm_inst', plot_color = 'Reds') #6th May 2024

plot_chart_with_metric(1, 'sfsm_inst', plot_color = 'Blues') #2nd Jan 2023
plot_chart_with_metric(53, 'sfsm_inst', plot_color = 'Blues') #1st Jan 2024
plot_chart_with_metric(71, 'sfsm_inst', plot_color = 'Blues') #6th May 2024

df_avg = df.groupby(['STATE', 'week_no']).mean().reset_index()
df_avg.to_csv('aggregated_by_state_data.csv')

df_avg['season'] = np.where(
    (df_avg['week_no'] >= 1) & (df_avg['week_no'] <= 13), 'Winter',
    np.where(
        (df_avg['week_no'] > 13) & (df_avg['week_no'] <= 26), 'Summer',
        np.where(
            (df_avg['week_no'] > 26) & (df_avg['week_no'] <= 39), 'Monsoon',
            np.where(
                (df_avg['week_no'] > 39) & (df_avg['week_no'] <= 48), 'Post-Monsoon',
                np.where(
                    (df_avg['week_no'] > 48) & (df_avg['week_no'] <= 65), 'Winter',
                    'Summer'  
                )
            )
        )
    )
)

df_avg.to_csv('aggregated_by_state_add_season.csv')
# plotting line chart in excel