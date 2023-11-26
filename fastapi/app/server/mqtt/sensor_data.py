from fastapi import APIRouter
# fastapi_mqtt
from fastapi_mqtt.fastmqtt import FastMQTT
from fastapi_mqtt.config import MQTTConfig
import json
import motor.motor_asyncio


from server.models.integrate_model import (
    ErrorResponseModel,
    ResponseModel,
    WaterSchema,
    UpdateWaterModel,
)
from server.integrateDB import (
    add_water,
    delete_water,
    retrieve_water,
    retrieve_waters,
    update_water,
)

mqtt_config = MQTTConfig(host="192.168.1.2",
                         port=1883,
                         keepalive=60,
                         username="TGR_GROUP11",
                         password="RL499P")

fast_mqtt = FastMQTT(config=mqtt_config)

router = APIRouter()

MONGO_DETAILS = "mongodb://mongoDB:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.integrate

water_collection = database.get_collection("test")

fast_mqtt.init_app(router)


@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    fast_mqtt.client.subscribe("/crmaA")  # subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)
    # print("1")


@fast_mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message from topic:", topic, "Payload", payload.decode())
    # mqtt_data = payload.decode()
    # print("MQTT_data : ", mqtt_data)
    # print("2")
    return 200


@fast_mqtt.subscribe("crmaA/btn")
async def message_to_topic(client, topic, payload, qos, properties):
    # print("Received message to specific topic: ", topic, payload.decode())
    data = json.loads(payload.decode())
    print(data)
    detect = data["value"]
    
    if detect == 'no obj':
        print("Obj not found")
        # nodetect = 0

        # all_data = {
        # "Day": 0,
        # "Height_S1": nodetect,
        # "Height_S3": 0,
        # "Discharge_S1": 0,
        # "Discharge_S2": 0,
        # "Discharge_S3": 0
        # }
        
        # print("if function ", detect)
        
        # waterheighdata: WaterSchema = all_data
        # await add_water(waterheighdata)
        return 200
    
    else:
        print("detection",data["value"])
    
    # hardwareField = await water_collection.find()
        user_def = [doc async for doc in water_collection.find({"Height_S1": 0})]
    
        print("hardwareField",user_def)
    
        min_day_object = min(user_def, key=lambda x: x['Day'])
        print("min_day_object",min_day_object)
        await water_collection.update_one(min_day_object,{"$set":{"Height_S1":int(detect)}})

        return 200
        



@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")
    # print("4")


@fast_mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)
    # print("5")


@router.get("/", response_description="test publish to mqtt")
async def publish_hello():
    return {"result": True, "message": "Subscribe"}


@router.post("/", response_description="ticker to mqtt")
async def publish_hello():
    ticker = {"ID": 117, "enable": "true"}
    fast_mqtt.publish("crmaA/cmd", ticker)  # publishing mqtt topic
    print("Published")
    return {"result": True, "message": "Ticker to capture"}
