import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://mongoDB:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.integrate

water_collection = database.get_collection("test")

def water_helper(water) -> dict:
    return {
        "id": str(water["_id"]),
        "Day": water.get('Day', ''),  # Use the get method with a default value
        "Height_S1": water.get("Height_S1", ''),
        "Height_S3": water.get("Height_S3", ''),
        "Discharge_S1": water.get("Discharge_S1", ''),
        "Discharge_S2": water.get("Discharge_S2", ''),
        "Discharge_S3": water.get("Discharge_S3", ''),
    }

# Retrieve all waters present in the database
async def retrieve_waters():
    waters = []
    async for water in water_collection.find():
        waters.append(water_helper(water))
    return waters


# Add a new water into to the database
async def add_water(water_data: dict) -> dict:
    water = await water_collection.insert_one(water_data)
    new_water = await water_collection.find_one({"_id": water.inserted_id})
    return water_helper(new_water)


# Retrieve a water data with a matching ID
async def retrieve_water(id: str) -> dict:
    water = await water_collection.find_one({"_id": ObjectId(id)})
    if water:
        return water_helper(water)


# Update a water with a matching ID
async def update_water(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    water = await water_collection.find_one({"_id": ObjectId(id)})
    if water:
        updated_water = await water_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_water:
            return True
        return False


# Delete a water from the database
async def delete_water(id: str):
    water = await water_collection.find_one({"_id": ObjectId(id)})
    if water:
        await water_collection.delete_one({"_id": ObjectId(id)})
        return True
