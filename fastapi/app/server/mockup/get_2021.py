import requests
import json
from fastapi import APIRouter 

from server.models.water import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

def split_ddmm(original_string):
    # Split the string into two parts
    date = str(original_string[:2])  # First two characters
    month = int(original_string[2:])  # Characters from index 2 to the end

    # Calculate next and last months
    next_month = (month % 12) + 1
    last_month = (month - 2) % 12 + 1

    return date, month, next_month, last_month

# Example usage:
original_string = "2809"
date, month, next_month, last_month = split_ddmm(original_string)

print(f"Date: {date}")
print(f"Month: {month}")
print(f"Next Month: {next_month}")
print(f"Last Month: {last_month}")

@router.get("/{DDMM}", response_description="water data retrieved")
async def get_mockup_data(DDMM):
    original_string = DDMM

    # Split the string into two parts
    date = int(original_string[:2])  # First two characters
    month = int(original_string[2:])  # Characters from index 2 to the end


    print(date, month)

    #url = 'http://192.168.10.159/v1/'+str(id)
    # url = 'https://jsonplaceholder.typicode.com/albums'#/'+str(id)
    
    url = 'https://api-v3.thaiwater.net/api/v1/thaiwater30/public/waterlevel_graph?station_type=tele_waterlevel&station_id=2752&start_date=2021-'+str(last_month)+'-'+str(date)+'&end_date=2021-'+str(next_month)+'-'+str(date)+'%2023:59'
    print(url)
    mockup = requests.get(url)
    if mockup:
        # print(json.loads(mockup.text))
        return ResponseModel(str(mockup.text), "API data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "data doesn't exist.")