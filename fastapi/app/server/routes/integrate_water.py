from fastapi import APIRouter, Body,Request
from fastapi.encoders import jsonable_encoder
import json
from server.integrateDB import (
    add_water,
    delete_water,
    retrieve_water,
    retrieve_waters,
    update_water,
)
from server.models.integrate_model import (
    ErrorResponseModel,
    ResponseModel,
    WaterSchema,
    UpdateWaterModel,
)
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://mongoDB:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.integrate

water_collection = database.get_collection("test")
router = APIRouter()

@router.post("/", response_description="Water data added into the database")
async def add_water_data(request: Request):
    await water_collection.delete_many({})
    rec = await request.body()
    recvData = json.loads(rec)
    result_list = [{'Day': Day['Day'], 'Height_S1': Height_S1['Height_S1'], 'Discharge_S1': Discharge_S1['Discharge_S1'], 'Discharge_S2': Discharge_S2['Discharge_S2'], 'Discharge_S3': Discharge_S3['Discharge_S3'], 'Height_S3': Height_S3['Height_S3']} for Day, Height_S1, Discharge_S1, Discharge_S2, Discharge_S3, Height_S3 in zip(recvData['Day'], recvData['Height_S1'], recvData['Discharge_S1'], recvData['Discharge_S2'], recvData['Discharge_S3'], recvData['Height_S3'])]

    print("water=====================")
    await water_collection.insert_many(result_list)
    print("status ++++++++++++++++++++++++")
    print("+++++++ RECORD SUCCESS ++++++++")

    return 200

    # return ResponseModel(new_water, "Water added successfully.")

@router.get("/", response_description="Waters retrieved")
async def get_waters():
    waters = await retrieve_waters()
    if waters:
        return ResponseModel(waters, "Waters data retrieved successfully")
    return ResponseModel(waters, "Empty list returned")


# @router.get("/{id}", response_description="Water data retrieved")
# async def get_water_data(id):
#     water = await retrieve_water(id)
#     if water:
#         return ResponseModel(water, "Water data retrieved successfully")
#     return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")


# @router.put("/{id}")
# async def update_water_data(id: str, req: UpdateWaterModel = Body(...)):
#     req = {k: v for k, v in req.dict().items() if v is not None}
#     updated_water = await update_water(id, req)
#     if updated_water:
#         return ResponseModel(
#             "Water with ID: {} name update is successful".format(id),
#             "Water name updated successfully",
#         )
#     return ErrorResponseModel(
#         "An error occurred",
#         404,
#         "There was an error updating the water data.",
#     )


# @router.delete("/{id}", response_description="Water data deleted from the database")
# async def delete_water_data(id: str):
#     deleted_water = await delete_water(id)
#     if deleted_water:
#         return ResponseModel(
#             "Water with ID: {} removed".format(id), "Water deleted successfully"
#         )
#     return ErrorResponseModel(
#         "An error occurred", 404, "Water with id {0} doesn't exist".format(id)
#     )
