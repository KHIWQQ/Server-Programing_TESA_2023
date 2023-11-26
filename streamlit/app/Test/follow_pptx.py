import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="House Rent Dashboard",
                    page_icon=":bar_chart:",
                    layout="wide")
df = pd.read_csv('House_Rent_Dataset.csv')

st.dataframe(df)


st.sidebar.header("Please Filter Here:")

city = st.sidebar.selectbox("Select the City:",
        options=df["City"].unique(),
        index=0
)

areaLocality = st.sidebar.multiselect("Select Area Locality:",
        options=df.query("City == @city")["Area_Locality"].unique(),
        default=df.query("City == @city")["Area_Locality"].unique()[0],
)
areaType = st.sidebar.selectbox("Select the Area Type:",
        options=df["Area_Type"].unique(),
        index=0
)
furnishing = st.sidebar.selectbox("Select the Furnishing Status:",
        options=df["Furnishing_Status"].unique(),
        index=0
)
df_selection = df.query(
        "Area_Locality == @areaLocality & Area_Type == @areaType & Furnishing_Status == @furnishing"
)
st.dataframe(df_selection) 
