import requests
import json
from fastapi import APIRouter 

from server.models.water import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

@router.get("/{id}", response_description="water data retrieved")
async def get_mockup_data(id):
    #url = 'http://192.168.10.159/v1/'+str(id)
    url = 'https://jsonplaceholder.typicode.com/albums/'+str(id)
    
    # url = 'https://api-v3.thaiwater.net/api/v1/thaiwater30/public/waterlevel_graph?station_type=tele_waterlevel&station_id=2752&start_date=2021-08-29&end_date=2021-10-28%2023:59'
    mockup = requests.get(url)
    if mockup:
        print(json.loads(mockup.text))
        return ResponseModel(str(mockup.text), "API data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "data doesn't exist.")