from typing import Optional
from pydantic import BaseModel, Field


class WaterSchema(BaseModel):
    Day: int
    Height_S1: float
    Height_S3: float
    Discharge_S1: float = Field(..., ge=0.0)
    Discharge_S2: float = Field(..., ge=0.0)
    Discharge_S3: float = Field(..., ge=0.0)

    class Config:
        schema_extra = {
            "example": {
            "Day": 99,
            "Height_S1": 111.0,
            "Height_S3": 111.0,
            "Discharge_S1": 1630.00,
            "Discharge_S2": 1011.40,
            "Discharge_S3": 3582
            }
        }


class UpdateWaterModel(BaseModel):
    Day: Optional[int]
    Height_S1: Optional[float]
    Height_S3: Optional[float]
    Discharge_S1: Optional[float]
    Discharge_S2: Optional[float]
    Discharge_S3: Optional[float]
    
    class Config:
        schema_extra = {
            "example": {
            "Day": 99,
            "Height_S1": 111.0,
            "Height_S3": 111.0,
            "Discharge_S1": 1630.00,
            "Discharge_S2": 1011.40,
            "Discharge_S3": 3582
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}