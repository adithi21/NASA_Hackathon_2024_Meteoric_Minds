
###############################33
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

