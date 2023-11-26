# import streamlit as st
# import pymongo
# import pandas as pd
# import numpy as np
# # MONGO_DETAILS = "mongodb://CRMA:1234@mongoDB:27017"

# st.title("Station Huana Dashboard")

# MONGO_DETAILS = "mongodb://mongoDB:27017"
# @st.cache_resource
# def init_connection():
#     print("connection successful")
#     return pymongo.MongoClient(MONGO_DETAILS)

# client = init_connection()

# @st.cache_data(ttl=600)
# def get_data():
#     db = client.integrate
#     item = db.predict.find()
#     print(item)
#     items = list(item)
#     df = pd.DataFrame(items)
#     return df

# items = get_data()
# st.dataframe(items)

# def get_year(year):
#     db = client.mockupdata
#     item = db.waterdata.find({"Year":year})
#     items = list(item)
#     df = pd.DataFrame(items)
#     return df

# def get_month(year, month):
   
#     db = client.mockupdata
#     item = db.waterdata.find({"Month":month,"Year":year})
#     items = list(item)
#     df = pd.DataFrame(items)
#     return df

# with st.sidebar:
#     st.write("Select Month to get data", color="#FFF")
#     month = st.slider('month', 1, 12, 12)
#     st.write("Select Year to get data")
#     year = st.slider('YEAR', 2017, 2023, 2023)
    
# def mean_dataFront(year):
#     db = client.mockupdata
#     item = db.waterdata.find({"Year":year})
#     items = list(item)
#     df = pd.DataFrame(items)
    
#     desired_column = "WaterDataFront"  # Replace with the actual column name
#     column_data = df[desired_column]
#     meanFront = df[desired_column].mean()
    
#     return meanFront

# def mean_dataBack(year):
#     db = client.mockupdata
#     item = db.waterdata.find({"Year":year})
#     items = list(item)
#     df = pd.DataFrame(items)
    
#     desired_column = "WaterDataBack"  # Replace with the actual column name
#     column_data = df[desired_column]
#     meanBack = df[desired_column].mean()
    
#     return meanBack

# def mean_dataDrain(year):
#     db = client.mockupdata
#     item = db.waterdata.find({"Year":year})
#     items = list(item)
#     df = pd.DataFrame(items)
    
#     desired_column = "WaterDrainRate"  # Replace with the actual column name
#     column_data = df[desired_column]
#     meanDrain = df[desired_column].mean()
    
#     return meanDrain

# items = get_year(year)
# items_M = get_month(year, month)
# # now
# Front = mean_dataFront(year)
# Back = mean_dataBack(year)
# Drain = mean_dataDrain(year)

# # old
# Front_old = mean_dataFront(year-1)    
# Back_old = mean_dataBack(year-1)
# Drain_old = mean_dataDrain(year-1)

# Front_2f = f"{Front_old:.2f}"
# Back_2f = f"{Back_old:.2f}"
# Drain_2f = f"{Drain_old:.2f}"

# # Percent
# per_Front = (Front-Front_old)/Front_old*100
# per_Back = (Back-Back_old)/Back_old*100
# per_Drain = (Drain-Drain_old)/Drain_old*100


# # Metrics
# col1, col2, col3 = st.columns(3)

# a = col1.metric("WaterDataFront AVG", Front_2f, per_Front )
# b = col2.metric("WaterDataBack AVG", Back_2f, per_Back )
# c = col3.metric("WaterDrainRate AVG", Drain_2f, per_Drain )

# tab1, tab2 = st.tabs(["📈 Year", "🗃 Month"])
# data = np.random.randn(10, 1)

# tab1.subheader("Year "+ str(year))
# items = get_year(year)
# tab1.dataframe(items)

# # Chart WaterDataFront
# tab1.title("Water Front")
# chart_data = pd.DataFrame(items, columns=["WaterDataFront"])
# tab1.area_chart(chart_data, color="#FF6347")

# # Chart WaterDataBack
# tab1.title("Water Back")
# chart_data = pd.DataFrame(items, columns=["WaterDataBack"])
# tab1.area_chart(chart_data, color="#2E8B57")

# # Chart WaterDataDrainRate
# tab1.title("Water Drain Rate")
# chart_data = pd.DataFrame(items, columns=["WaterDrainRate"])
# tab1.area_chart(chart_data)

# tab2.subheader("Month "+ str(month))
# items_M = get_month(year, month)
# tab2.dataframe(items_M)
# # Chart WaterDataFront
# tab2.title("Water Front")
# chart_data = pd.DataFrame(items_M, columns=["WaterDataFront"])
# tab2.bar_chart(chart_data, color="#FF6347")

# # Chart WaterDataBack
# tab2.title("Water Back")
# chart_data = pd.DataFrame(items_M, columns=["WaterDataBack"])
# tab2.bar_chart(chart_data, color="#2E8B57")

# # Chart WaterDataDrainRate
# tab2.title("Water Drain Rate")
# chart_data = pd.DataFrame(items_M, columns=["WaterDrainRate"])
# tab2.bar_chart(chart_data)
import streamlit as st
import pymongo
import pandas as pd
import numpy as np
import pydeck as pdk

st.title(":ocean: Emergency Flood Alert System")
    
MONGO_DETAILS = "mongodb://mongoDB:27017"
@st.cache_resource
def init_connection():
    print("connection successful")
    return pymongo.MongoClient(MONGO_DETAILS)

client = init_connection()

@st.cache_data(ttl=1)

def get_data():
    db = client.integrate
    item = db.test.find()
    items = list(item)
    df = pd.DataFrame(items)
    return df

st.snow()

data = get_data()
chart_data = pd.DataFrame(data, columns=["Discharge_S1","Discharge_S2", "Discharge_S3"])

st.line_chart(chart_data)

# st.dataframe(data)
selected_columns = ['Day', 'Height_S1','Height_S3','Discharge_S1','Discharge_S2','Discharge_S3']
df_selected = data[selected_columns]
# st.dataframe(df_selected)

HS1 = data["Height_S1"].mean()
HS3 = data["Height_S3"].mean()
DS1 = data["Discharge_S1"].mean()
DS2 = data["Discharge_S2"].mean()
DS3 = data["Discharge_S3"].mean()

HS1 = f"{HS1:.2f}"
HS3 = f"{HS3:.2f}"
DS1 = f"{DS1:.2f}"
DS2 = f"{DS2:.2f}"
DS3 = f"{DS3:.2f}"


tab1, tab2, tab3, tab4  = st.tabs(["Map","Height_Station", "Discharge Station","Dataframe"])

with tab1:
   st.header("Map")
with tab2:
   col1, col2, col3 = st.columns(3)
   col1.metric("Height_S1", HS1, "1.2 °F")
   col2.metric("Height_S2", "No Data")
   col3.metric("Height_S3", HS3, "-8%")
  
with tab3:
   col1, col2, col3 = st.columns(3)
   col1.metric("Discharge_S1", DS1, "1.2 °F")
   col2.metric("Discharge_S2", DS2, "-8%")
   col3.metric("Discharge_S3", DS3, "4%")

with tab4:
    st.dataframe(df_selected)
  
with st.sidebar:
    st.sidebar.markdown(
    """<style>
    .sidebar-text {
        color: white; /* Change this to the color you prefer */
    }
    </style>"""
    ,
    unsafe_allow_html=True
    )
    
    st.sidebar.markdown('<p class="sidebar-text">Day.</p>', unsafe_allow_html=True)

    #st.write("Day")
    number = st.number_input("Day:sun_with_face:",1,31, placeholder="Type a number...")
    st.write('The current day is ', number)

    st.write("Select Month to get data")
    month = st.slider('month', 1, 12, 12)
# st.dataframe(data)