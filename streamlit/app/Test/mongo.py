import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string

# Specify the database and collection
db = client["water"]  # Replace with your database name
collection = db["water_collection"]  # Replace with your collection name

# Query MongoDB to retrieve data
# For example, get all documents in the collection
cursor = collection.find({})

# Iterate over the cursor and print each document
for document in cursor:
    print(document)

# Close the MongoDB connection (optional)
client.close()
