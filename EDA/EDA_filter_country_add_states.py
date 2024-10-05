import pandas as pd
import numpy as np
import os

from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import geodatasets

import matplotlib.pyplot as plt
import descartes

df = pd.read_csv("C:/Users/ADITHI/Desktop/nasa/gws/NASA_Hackathon_2024_Meteoric_Minds/India_gws_01012023_05092024.csv")

df.shape 
# 677618, 8

df.head(2)
df.columns

df[df.duplicated()].shape

df['week_no'] = df.time.rank(method='dense').astype(int)
# add week no int

geometry = [Point(xy) for xy in zip(df.loc[df.week_no == 74,'lon'], df.loc[df.week_no == 74,'lat'])]
gdf = GeoDataFrame(df.loc[df.week_no == 74, ], geometry=geometry)   

#this is a simple map that goes with geopandas
# deprecated: world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = gpd.read_file(geodatasets.data.naturalearth.land['url'])
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)


street_map = gpd.read_file('C:/Users/ADITHI/Desktop/nasa/gws/NASA_Hackathon_2024_Meteoric_Minds/EDA/india_st.shp')
fig, ax = plt.subplots(figsize=(15,15))
street_map.plot(ax=ax)

geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
crs = {'init':'epsg:4326'}
geo_df = GeoDataFrame(df, #specify our data
                      crs=crs, #specify our coordinate reference system
                      geometry=geometry) #specify the geometry list we created
geo_df.head()

fig, ax = plt.subplots(figsize=(15,15))
street_map.plot(ax=ax, alpha=0.4, color='grey')
geo_df.plot(ax=ax, markersize=20, color='blue', marker='o', label='Neg')

country_map = gpd.read_file('C:/Users/ADITHI/Desktop/nasa/gws/NASA_Hackathon_2024_Meteoric_Minds/EDA/india_ds.shp')
# Assuming your DataFrame has geometry information
gdf = GeoDataFrame(df, crs=crs
, geometry= [Point(xy) for xy in zip(df['lon'], df['lat'])])

# Filter the DataFrame
filtered_gdf = gdf[gdf.within(country_map.unary_union)]

# Convert back to a regular DataFrame if needed
filtered_df = pd.DataFrame(filtered_gdf)
world = gpd.read_file(geodatasets.data.naturalearth.land['url'])
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)


df_state = gpd.sjoin(filtered_gdf, street_map, how="right")

df_state = df_state[['lat', 'lon', 'time', 'gws_inst', 'rtzsm_inst',
       'sfsm_inst', 'start_date', 'end_date', 'week_no', 'STATE']]

df_state.to_csv('C:/Users/ADITHI/Desktop/nasa/gws/NASA_Hackathon_2024_Meteoric_Minds/data_with_state.csv')





