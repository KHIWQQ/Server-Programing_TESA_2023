import streamlit as st
import pymongo
import pandas as pd
import numpy as np
import pydeck as pdk
from PIL import Image

#image = Image.open('image.jpg')

#st.image(image, caption='Sunrise by the mountains')

st.title(":ocean: EFAAS :ocean:")
    
MONGO_DETAILS = "mongodb://mongoDB:27017"
@st.cache_resource
def init_connection():
    print("connection successful")
    return pymongo.MongoClient(MONGO_DETAILS)

client = init_connection()

@st.cache_data(ttl=600)
def get_data():
    db = client.waterwater
    item = db.flood.find()
    items = list(item)
    df = pd.DataFrame(items)
    return df

#st.balloons()

def get_map():
    db = client.waterwater
    item = db.map.find()
    items = list(item)
    df = pd.DataFrame(items)
    return df

def get_mapdataS1(lats1,lons1):
    db = client.waterwater
    item = db.map.find({"Lat_S1":lats1,"Lon_S1":lons1})
    items = list(item)
    df = pd.DataFrame(items)
    return df

def get_date(date):
    db = client.waterwater
    item = db.flood.find({"Day":date})
    items = list(item)
    df = pd.DataFrame(items)
    # st.dataframe(items)
    return df

with st.sidebar:
    # image = Image.open('image.jpg')
    # st.image(image, caption='Sunrise by the mountains')
    st.header(':ocean: Emergency Fast Alert System', divider='blue')
    st.header('Presented by :orange[CRMA Robotic] :red[A]')
    st.write(":calendar: :blue[Select Day to get data]")
    date = st.slider('Day', 1, 65, 65)

maping = get_map()
date_date = get_date(date)
data = get_data()
chart_data = pd.DataFrame(data, columns=["Discharge_S1","Discharge_S2", "Discharge_S3"])
st.line_chart(chart_data)

show_date = get_date(date)
#st.write(show_date)
#st.dataframe(show_date["Height_S1"])
select_s1 = ['Day','Lat_S1','Lon_S1','Height_S1','Discharge_S1']
df_maps1 = maping[select_s1]
select_ds1 = ['Day','Lat_S1','Lon_S1','Discharge_S1']
df_mapds1 = maping[select_ds1]
select_s2 = ['Day','Lat_S2','Lon_S2','Discharge_S2']
df_maps2 = maping[select_s2]
select_ds2 = ['Day','Lat_S2','Lon_S2','Discharge_S2']
df_mapds2 = maping[select_ds2]
select_s3 = ['Day','Lat_S3','Lon_S3','Height_S3','Discharge_S3']
df_maps3 = maping[select_s3]
select_ds3 = ['Day','Lat_S3','Lon_S3','Discharge_S3']
df_mapds3 = maping[select_ds3]
# st.dataframe(data)
selected_columns = ['Day', 'Height_S1','Height_S3','Discharge_S1','Discharge_S2','Discharge_S3']
df_selected = data[selected_columns]
# st.dataframe(df_selected)
#
#Lat

#Date for Data
date_HS1 = show_date["Height_S1"]
date_HS3 = show_date["Height_S3"]
date_DS1 = show_date["Discharge_S1"]
date_DS2 = show_date["Discharge_S2"]
date_DS3 = show_date["Discharge_S3"]

#Mean
HS1 = data["Height_S1"].mean()
HS3 = data["Height_S3"].mean()
DS1 = data["Discharge_S1"].mean()
DS2 = data["Discharge_S2"].mean()
DS3 = data["Discharge_S2"].mean()
#Max
Max_HS1 = data["Height_S1"].max()
Max_HS3 = data["Height_S3"].max()
Max_DS1 = data["Discharge_S1"].max()
Max_DS2 = data["Discharge_S2"].max()
Max_DS3 = data["Discharge_S2"].max()
#Max of Date
Max_date_HS1 = date_HS1.max()
Max_date_HS3 = date_HS3.max()
Max_date_DS1 = date_DS1.max()
Max_date_DS2 = date_DS2.max()
Max_date_DS3 = date_DS3.max()
#Min
Min_HS1 = data["Height_S1"].min()
Min_HS3 = data["Height_S3"].min()
Min_DS1 = data["Discharge_S1"].min()
Min_DS2 = data["Discharge_S2"].min()
Min_DS3 = data["Discharge_S2"].min()
#2f
HS1 = f"{HS1:.2f}"
HS3 = f"{HS3:.2f}"
DS1 = f"{DS1:.2f}"
DS2 = f"{DS2:.2f}"
DS3 = f"{DS3:.2f}"


# st.write("Height_S1 mean ",data["Height_S1"].mean())
# st.write("Height_S3 mean ",data["Height_S3"].mean())
# st.write("Discharge_S1 mean ",data["Discharge_S1"].mean())
# st.write("Discharge_S2 mean ",data["Discharge_S2"].mean())
# st.write("Discharge_S3 mean ",data["Discharge_S3"].mean())

tab1, tab2, tab3, tab4  = st.tabs(["Map","Height_Station", "Discharge Station","Dataframe"])

with tab1:
   st.header("Map Ubonratchathani")
#    df = pd.DataFrame({
#     "col1":15.223191442234949 , 15.31939466741273 , 15.223191442234949,
#     "col2":104.85724926663899 , 104.45790510591928 , 104.85724926663899,
#     "col3": np.random.randn(1000) * 100,
#     "col4": np.random.rand(1000, 4).tolist(),
#     }) 
#    st.map(df,
#         latitude='col1',
#         longitude='col2',
#         size='col3',
#         color='col4') 

with tab2:
   col1, col2, col3 = st.columns(3)
   col1.metric("Height_S1 Day:",date_HS1,Max_HS1,"off")
   col2.metric("Height_S2", "No Data")
   col3.metric("Height_S3",date_HS3,Max_HS3,"off")
  
with tab3:
   col1, col2, col3 = st.columns(3)
   col1.metric("Discharge_S1", date_DS1, Max_DS1,"off")
   col2.metric("Discharge_S2",date_DS2, Max_DS2,"off")
   col3.metric("Discharge_S3",date_DS3, Max_DS3,"off")

with tab4:
    st.dataframe(df_selected)
  
    # st.write("Select Month to get data")
    # month = st.selectbox('month', 1, 12, 12)

# with st.container():
#     st.write("This is inside the container") 
#     with st.sidebar:
#         #st.image(image)
#         st.sidebar.markdown(
#         """<style>
#         .sidebar-text {
#             color: white; /* Change this to the color you prefer */
#         }
#         </style>"""
#         ,
#         unsafe_allow_html=True
#         )

#         st.sidebar.markdown('<p class="sidebar-text">Day.</p>', unsafe_allow_html=True)

#         #st.write("Day")
#         number = st.number_input(":orange[Day:sun_with_face:]",1,31, placeholder="Type a number...")
#         # st.write('The current day is ', number)

#         html=f'''<p style="color:white">The current day is <div style='background-color:yellow '>{number}</div> </p>'''
#         st.markdown(html, unsafe_allow_html=True)

#         st.write("Select Month to get data", color="#FFFFFF")
#         month = st.slider('month', 1, 12, 12)
# st.dataframe(data)

#GHAS1 = get_HS1()
#st.dataframe(GHAS1)

# chart_data = pd.DataFrame(
#     get_data() + [15.223191442234949,104.85724926663899],
#     columns=['lat', 'lon'])

# st.pydeck_chart(pdk.Deck(
#         map_style=None,
#         initial_view_state=pdk.ViewState(
#             latitude=15.223191442234949,
#             longitude=104.85724926663899,
#             zoom=11,
#             pitch=50,
#         ),
#         layers=[
#             pdk.Layer(
#             'HexagonLayer',
#             data=chart_data,
#             get_position='[lon, lat]',
#             radius=200,
#             elevation_scale=4,
#             elevation_range=[0, 1000],
#             pickable=True,
#             extruded=True,
#             ),
#             pdk.Layer(
#                 'ScatterplotLayer',
#                 data=chart_data,
#                 get_position='[lon, lat]',
#                 get_color='[200, 30, 0, 160]',
#                 get_radius=200,
#             ),
#         ],
#     ))

# chart_data = pd.DataFrame(data, columns=["Discharge_S1","Discharge_S2", "Discharge_S3"])

# st.line_chart(chart_data)

# lnhs1 = pd.DataFrame(items, columns=["Height_S1"])
# st.line_chart(lnhs1, color="#FF6347")
# lnhs3 = pd.DataFrame(items, columns=["Height_S3"])
# st.line_chart(lnhs3, color="#FF6347")

# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [15.223191442234949, 104.85724926663899],
#     columns=['lat', 'lon'])


#st.map(data,15.223191442234949,104.85724926663899)
# df = pd.DataFrame({
#     "col1": np.random.randn(1000) / 50 + 15.223191442234949,
#     "col2": np.random.randn(1000) / 50 + 104.85724926663899,
#     "col3": np.random.randn(1000) * 100,
#     "col4": np.random.rand(1000, 4).tolist(),
# })

# st.map(df,
#     latitude='col1',
#     longitude='col2',
#     size='col3',
#     color='col4')

#st.dataframe.map()
#15.131918934446878, 104.70494657693382   S1
#15.31939466741273, 104.45790510591928    S2
#15.223191442234949, 104.85724926663899   S3