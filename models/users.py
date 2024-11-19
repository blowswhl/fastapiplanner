from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "Password": "strong!!!",
                "evnets": [],

            }
        }


class UserSignIn(BaseModel):
    email: EmailStr 
    password: str 

    class Config: 
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }