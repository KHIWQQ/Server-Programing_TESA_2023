import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["water"]  # Replace with your database name
collection = db["water_collection"]  # Replace with your collection name

# Query MongoDB and convert results to DataFrame
cursor = collection.find({})
df = pd.DataFrame(list(cursor))

# Display the DataFrame using Streamlit
st.title("MongoDB Data in Streamlit")
st.dataframe(df)
