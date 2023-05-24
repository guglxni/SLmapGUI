import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("gps_coordinates.csv")

# Get the latitude and longitude columns
latitude = df["latitude"]
longitude = df["longitude"]

# Plot the trajectory
plt.plot(latitude, longitude)
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.title("Trajectory")

# Show the plot
st.pyplot(plt)

