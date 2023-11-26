import streamlit as st
import pymongo
import pandas as pd
import numpy as np
import pydeck as pdk

st.title(":ocean: Flood Monitoring Smart system")
    
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

with st.sidebar:
    # image = Image.open('image.jpg')
    # st.image(image, caption='Sunrise by the mountains')
    st.image("https://www.crma.ac.th/wp-content/uploads/2023/06/crma_logo.png")
    st.header(':ocean: Ubon F M O S S', divider='blue')
    # Flood Monitoring Smart system
    # st.header('Presented by :orange[CRMA Robotic] :red[A]')
    st.write(":calendar: :blue[Select Day to get data]")
    date = st.slider('Day', 1, 60, 40)
    st.header('Presented by :orange[CRMA Robotic] :red[A]')
   
def get_by_date(date):
    db = client.integrate
    item = db.test.find({"Day":date})
    items = list(item)
    df = pd.DataFrame(items)
    return df    
# st.snow()

data = get_data()
by_date = get_by_date(date)
back = (date-1)
old_date = get_by_date(int(back))

A = int(by_date["Height_S3"])

def alert():
    if A > 112:
        # st.write("alert")
        st.error('S3 Station is Danger', icon="🚨")
        
    elif A > 108:
        # st.write("secure")   
        st.warning('Warning', icon="⚠️")
        
    else:
        st.success('S3 Station is Safe', icon="✅")
        
alert()       
# st.write(int(by_date["Height_S3"]))
# Test dataframe
# def show_alert():
#     if data["Height_S3"] >= 112:
#         st.dataframe(data)
# show_alert()
chart_Discharge = pd.DataFrame(data, columns=["Discharge_S1","Discharge_S2", "Discharge_S3","Day"])
chart_Height = pd.DataFrame(data, columns=["Height_S1","Height_S3","Day"])
# st.line_chart(chart_data, x="Day")

# st.dataframe(data)
selected_columns = ['Day', 'Height_S1','Height_S3','Discharge_S1','Discharge_S2','Discharge_S3']
df_selected = data[selected_columns]
# st.dataframe(df_selected)

HS1M = data["Height_S1"].max()
HS3M = data["Height_S3"].max()
DS1M = data["Discharge_S1"].max()
DS2M = data["Discharge_S2"].max()
DS3M = data["Discharge_S3"].max()

HS1 = by_date["Height_S1"]
HS3 = by_date["Height_S3"]
DS1 = by_date["Discharge_S1"]
DS2 = by_date["Discharge_S2"]
DS3 = by_date["Discharge_S3"]

HS1 = round(float(HS1), 2)
HS3 = round(float(HS3), 2)
DS1 = round(float(DS1), 2)
DS2 = round(float(DS2), 2)
DS3 = round(float(DS3), 2)

HS1M = round(float(HS1M), 2)
HS3M = round(float(HS3M), 2)
DS1M = round(float(DS1M), 2)
DS2M = round(float(DS2M), 2)
DS3M = round(float(DS3M), 2)
# HS1F = f"{HS1:.2f}"
# HS3 = f"{HS3:.2f}"
# DS1 = f"{DS1:.2f}"
# DS2 = f"{DS2:.2f}"
# DS3 = f"{DS3:.2f}"

# st.header("อัตราการไหลของน้ำในแต่ละสถานีของวันที่", int(date))
tab1, tab2, tab3  = st.tabs(["Discharge Station","Height_Station","Dataframe"])

with tab1:
   st.line_chart(chart_Discharge, x="Day")
   col1, col2, col3 = st.columns(3)
   col1.metric("Discharge_S1", DS1, DS1M)
   col2.metric("Discharge_S2", DS2, DS2M)
   col3.metric("Discharge_S3", DS3, DS3M)
   
with tab2:
   st.line_chart(chart_Height, x="Day")
   col1, col2, col3 = st.columns(3)
   col1.metric("Height_S1", str(HS1)+"  m.", str(HS1M)+"  m.")
   col2.metric("Height_S2", "NaN", "NaN")
   col3.metric("Height_S3", str(HS3)+"  m.", str(HS3M)+"  m.")
  
with tab3:
    st.dataframe(df_selected)
  