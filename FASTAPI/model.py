import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Book(BaseModel):
    id: str = Field(...)
    title: str = Field(...)
    author: str = Field(...)
    year: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "1984",
                "author": "George Orwell", 
                "year": "1949"
            }
        }

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    year: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "1984",
                "author": "George Orwell", 
                "year": "1949"
            }
        }