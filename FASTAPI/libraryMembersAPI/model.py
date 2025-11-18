import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Member(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str = Field(...)
    email: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",               
                "name": "Brad Pitt",
                "email": "bpitt@library.com", 
            }
        }    

class MemberCreate(BaseModel):
    name: str = Field(...)
    email: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Brad Pitt",
                "email": "bpitt@library.com", 
            }
        }

class MemberUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Brad Pitt",
                "email": "bpitt@library.com", 
            }
        }