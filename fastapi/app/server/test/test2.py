from pymongo import MongoClient
import random

class MongoDB(object):
    def __init__(self, host='mongoDB', port=27017, database_name="integrate", collection_name="test"):
        try:
            self._connection = MongoClient(host=host, port=port, maxPoolSize=200)
        except Exception as error:
            raise Exception(error)
        self._database = None
        self._collection = None
        if database_name:
            self._database = self._connection[database_name]
        if collection_name:
            self._collection = self._database[collection_name]

    def insert(self, post):
        # add/append/new single record
        post_id = self._collection.insert_one(post).inserted_id
        return post_id

def water_helper(water) -> dict:
    return {
        "Day": water["Day"],
        "Height_S1": water["Height_S1"],
        "Height_S3": water["Height_S3"],
        "Discharge_S1": water["Discharge_S1"],
        "Discharge_S2": water["Discharge_S2"],
        "Discharge_S3": water["Discharge_S3"],
    }

# Example usage
data_list = list()
for day in range(1, 4):  # Adjust the range as needed
    data_list.append({
        "Day": [{"Day": day}],
        "Height_S1": [{"Height_S1": random.uniform(115, 120) for _ in range(3)}],
        "Height_S3": [{"Height_S3": random.uniform(115, 120) for _ in range(3)}],
        "Discharge_S1": [{"Discharge_S1": random.uniform(1500, 1600) for _ in range(3)}],
        "Discharge_S2": [{"Discharge_S2": random.uniform(900, 1000) for _ in range(3)}],
        "Discharge_S3": [{"Discharge_S3": random.uniform(3400, 3600) for _ in range(3)}],
    })

print('[*] Pushing data to MongoDB ')
mongo_db = MongoDB()

for water_item in data_list:
    print('[!] Inserting - ', water_item)
    mongo_db.insert(water_helper(water_item))
