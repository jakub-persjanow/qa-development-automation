from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List, Dict, Tuple, Text

from model import Member, MemberCreate, MemberUpdate

router = APIRouter()

@router.post("/", response_description="Create new member", status_code=status.HTTP_201_CREATED, response_model=Member)
def create_member(request: Request, member: MemberCreate  = Body(...)):
    new_member = Member(**member.dict())
    member_dict = jsonable_encoder(new_member)
    result = request.app.database["libraryMembers"].insert_one(member_dict)
    created_member = request.app.database["libraryMembers"].find_one({"_id": result.inserted_id})
    created_member["_id"] = str(created_member["_id"])

    return created_member

@router.get("/", response_description="Get all members", response_model=List[Member])
def list_members(request: Request):
    members = list(request.app.database["libraryMembers"].find(limit=100))
    return members

@router.get("/{id}", response_description="Get a single members providing id", response_model=Member)
def find_member(id: str, request: Request):
    if (member := request.app.database["libraryMembers"].find_one({"id": id})) is not None:
        return member
    raise   HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Member with id {id} not found")

@router.put("/{id}", response_description="Update existing member", response_model=Member)
def update_member(id: str, request: Request, member: MemberUpdate = Body(...)):
    member = {k: v for k, v in member.dict().items() if v is not None}
    if len(member) >= 1:
        update_result = request.app.database["libraryMembers"].update_one(
            {"id": id}, {"$set": member}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Member with ID {id} not found")

    if (
        existing_member := request.app.database["libraryMembers"].find_one({"id": id})
    ) is not None:
        return existing_member

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Member with ID {id} not found")

@router.delete("/{id}", response_description="Delete member")
def delete_member(id: str, request: Request, response: Response):
    delete_result = request.app.database["libraryMembers"].delete_one({"id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Member with ID {id} not found")