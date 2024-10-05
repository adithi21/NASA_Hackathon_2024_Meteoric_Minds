
###############################33#
#for full data
import xarray as xr
import pandas as pd
from datetime import datetime, timedelta
import glob

# Path to the directory containing the .nc4 files
folder_path = 'agri_gws_data/*.nc4'

# List to store the DataFrames for all files
all_dataframes = []

# Loop through all .nc4 files in the specified folder
for file in glob.glob(folder_path):
    # Extract the date from the filename
    filename = file.split('/')[-1]  # Get the filename from the path
    date_str = filename.split('.')[1][1:]  # Extract the date part (e.g., 20240527)

    # Convert the string to a datetime object
    start_date = datetime.strptime(date_str, '%Y%m%d')

    # Calculate the end date (one week later)
    end_date = start_date + timedelta(days=6)

    # Open the dataset
    dataset = xr.open_dataset(file)

    # Convert the selected variables to a DataFrame and reset the index
    df = dataset[['lat', 'lon', 'time', 'gws_inst', 'rtzsm_inst', 'sfsm_inst']].to_dataframe().reset_index()

    # Add the start and end date columns
    df['start_date'] = start_date
    df['end_date'] = end_date

    # Optionally, remove rows where any of the selected variables are NaN
    df_non_null = df.dropna(subset=['gws_inst', 'rtzsm_inst', 'sfsm_inst'])

    # Append the DataFrame to the list
    all_dataframes.append(df_non_null)

# Concatenate all DataFrames into a single DataFrame
final_dataframe = pd.concat(all_dataframes, ignore_index=True)

# Display the final DataFrame with selected variables
print("Final DataFrame for all files with lat, lon, time, gws_inst, rtzsm_inst, sfsm_inst, start_date, and end_date:")
print(final_dataframe)

# Define the start and end dates for filtering
start_date = '2023-01-01'
end_date = '2024-12-31'

# Filter the DataFrame to include only rows where 'time' is between 2023 and 2024
filtered_df = final_dataframe[(final_dataframe['time'] >= start_date) & (final_dataframe['time'] <= end_date)]

filtered_df.shape
#######
import geopandas as gp
import geoviews as gv
from geoviews import opts, tile_sources as gvts
import holoviews as hv
gv.extension('bokeh', 'matplotlib')
# import shapely
# import warnings
# from shapely.errors import ShapelyDeprecationWarning
# warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)


india_aprox = gp.GeoDataFrame.from_file('agri_gws_data/india-osm.geojson') 

india_aprox['geometry'][0] 


# india_temp = gp.read_file('agri_gws_data/India_Country_Boundary.shx') 

# Create a bounding box of India boundary
bounds = india_aprox.total_bounds  # (minx, miny, maxx, maxy)

# Filter points within the bounding box before more detailed spatial operations
points_within_bbox = filtered_df[
    (filtered_df['lon'] >= bounds[0]) & (filtered_df['lon'] <= bounds[2]) &
    (filtered_df['lat'] >= bounds[1]) & (filtered_df['lat'] <= bounds[3])
]


points_within_bbox.to_csv('India_gws_01012023_05092024.csv')

# # Create a list of geodataframe columns to be included as attributes in the output mapp
# vdims = []
# for f in final_dataframe:
#     print(f)
#     if f not in ['geometry']:
#         vdims.append(f)

# vdims.shape

# pd.DataFrame(vdims).shape
# # Call the function for plotting the GRACE points
# gv.Polygons(india_aprox['geometry']).opts(line_color='red', color=None) * pointVisual(latslons, vdims = vdims)

##########################################3
###############################33

# import geopandas as gpd
# import pandas as pd
# from shapely.geometry import Point



# # Convert 'lat' and 'lon' to a GeoSeries of Points
# geometry = [Point(xy) for xy in zip(points_within_bbox['lon'], points_within_bbox['lat'])]

# # Create a GeoDataFrame from your DataFrame
# gdf_points = gpd.GeoDataFrame(points_within_bbox, geometry=geometry, crs=india_aprox.crs)

# # Get the boundary geometry of India (assuming a single shape in the GeoDataFrame)
# india_boundary = india_aprox['geometry'][0]

# # Filter points that are within the boundary of India
# points_within_india = gdf_points[gdf_points.geometry.within(india_boundary)]

# # Display or use the filtered points
# print(points_within_india)