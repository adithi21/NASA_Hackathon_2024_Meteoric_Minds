import streamlit as st
import numpy as np
import pickle
import tensorflow as tf
import pydeck as pdk

# Load the saved model
with open('st_cnn_path.pkl', 'rb') as file:
    model_path = pickle.load(file)

model = tf.keras.models.load_model(model_path)

# App Title
st.title('Groundwater Storage with intercative map')

# # Define input fields for user to enter values (adjust based on your model's requirements)
# st.write("Enter input values for prediction:")

# # Example: Assuming the model expects 3 features per input (adjust this according to your model's input shape)
# try:
#     feature_1 = st.number_input("Feature 1" )
#     feature_2 = st.number_input("Feature 2")
#     feature_3 = st.number_input("Feature 3")

#     # Collect input as a numpy array
#     user_input = np.array([[feature_1, feature_2, feature_3]])

#     # Reshape input to match the model's expected input shape (e.g., (1, 1, 3))
#     user_input_reshaped = user_input.reshape(1, 1, 3)  # Adjust this shape based on your model

#     # Make predictions using the model
#     if st.button("Predict"):
#         predictions = model.predict(user_input_reshaped)
#         st.write("Predicted Groundwater Storage:")
#         st.dataframe(predictions)

# except Exception as e:
#     st.error(f"An error occurred: {e}")



#############################################################33
#map
import pandas as pd
# Load the dataset
data = pd.read_csv('data_with_state.csv')

data1=data.iloc[:,:2]

# # Define the initial view
# initial_view = pdk.ViewState(
#     latitude=data1['lat'].mean(),
#     longitude=data1['lon'].mean(),
#     zoom=4,
#     pitch=0,
# )

# # Create a layer to display the points
# layer = pdk.Layer(
#     "ScatterplotLayer",
#     data1,
#     get_position='[lon, lat]',
#     get_color='[255, 0, 0, 160]',
#     get_radius=200000,
#     pickable=True,
# )

# # Create the deck.gl map
# deck = pdk.Deck(layers=[layer], initial_view_state=initial_view)

# # Render the map
# st.pydeck_chart(deck)

# # Handle click events
# clicked_point = st.session_state.get("clicked_point", None)

# if clicked_point:
#     lat, lon = clicked_point
#     st.write(f"Latitude: {lat}, Longitude: {lon}")

# # Create a callback function for click events
# def on_click(event):
#     st.session_state.clicked_point = (event['lat'], event['lon'])

# # Register the callback
# deck.on_click(on_click)


#################################################3
# Sample code to display the map (replace with your actual map)
st.map(data[['lat', 'lon']])

# # Get distinct values of latitudes and longitudes
# distinct_values = data[['lat', 'lon']].drop_duplicates()
# # Display the first three rows
# st.dataframe(distinct_values)

# Input fields for latitude and longitude
# Title for the app
st.title("Input Week Number")

# User input for week number
week_number = st.text_input("Please enter the week number you want to forecast:")

lat = st.number_input("Enter Latitude:", format="%.6f")
lon = st.number_input("Enter Longitude:", format="%.6f")

# Create a DataFrame with the entered lat and lon for plotting
user_location = pd.DataFrame({'lat': [lat], 'lon': [lon]})

    # Display the map centered on the user-provided coordinates
st.map(user_location)

# You can also filter data based on the entered latitude and longitude
if st.button("Get Closest State"):
    # You could implement logic to find the closest state based on the entered lat/lon
    closest_state = data.loc[(data['lat'] - lat).abs().idxmin(), 'STATE']
    st.write(f"The closest state to the entered coordinates is: {closest_state}")

