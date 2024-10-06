import streamlit as st
import numpy as np
import pickle
import tensorflow as tf

# Load the saved model
with open('st_cnn_path.pkl', 'rb') as file:
    model_path = pickle.load(file)

model = tf.keras.models.load_model(model_path)

# App Title
st.title('Groundwater Storage Prediction using ST-CNN')

# Define input fields for user to enter values (adjust based on your model's requirements)
st.write("Enter input values for prediction:")

# Example: Assuming the model expects 3 features per input (adjust this according to your model's input shape)
try:
    feature_1 = st.number_input("Feature 1" )
    feature_2 = st.number_input("Feature 2")
    feature_3 = st.number_input("Feature 3")

    # Collect input as a numpy array
    user_input = np.array([[feature_1, feature_2, feature_3]])

    # Reshape input to match the model's expected input shape (e.g., (1, 1, 3))
    user_input_reshaped = user_input.reshape(1, 1, 3)  # Adjust this shape based on your model

    # Make predictions using the model
    if st.button("Predict"):
        predictions = model.predict(user_input_reshaped)
        st.write("Predicted Groundwater Storage:")
        st.dataframe(predictions)

except Exception as e:
    st.error(f"An error occurred: {e}")

