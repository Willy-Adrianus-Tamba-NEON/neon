from asyncio.windows_events import NULL
import json
from unittest import result
from fastapi import APIRouter, Body, Response
from apps.controllers.FiraController import ControllerFira as Fira

router = APIRouter()

data_input = json.dumps({
    "loanid": "100400",
    "loan_type": "2",
    "loan_status": "1",
    "loan_amount": "5000",
    "loan_tenure": "20",
    "interest": "15",
    "cif": "980789",
    "idno": "123456789",
    "fname": "Fira",
    "lname": "Sukmanisa",
    "dob": "1999/08/16",
    "gender": "Female",
    "marital_status": "Single",
    "income": 70000,
    "phone": "123-456-789",
    "email": "firasukmanisa@gmail.com",
    "isphoneverified": 0,
    "isemailverified": 0,
    "createdate": "2021/01/25",
    "updatedate": "2021/01/25",
    "source": "Web",
}, indent=2)

@router.get("/get_user_by_cif")
async def get_user_by_cif(response: Response, cif:str):
    result = Fira.get_user_by_cif(cif= cif)
    return result


@router.post("/insert_new_data")
async def insert_new_data(response: Response, input_data=Body(..., example=data_input)):
    result = Fira.insert_new_data(input_data=input_data)
    return result

data_update = json.dumps({
    "fname": "Fira",
    "lname": "Sukmanisa",
    "gender": "Female",
    "marital_status": "Married",
    "email": "firasukmanisa@gmail.com",
    "isphoneverified": 1,
    "isemailverified": 1,
})

@router.put("/edit_user")
async def edit_by_cif(response: Response,cif:str, data_update=Body(..., example=data_update)):
    result = Fira.edit_by_cif(cif=cif, data_update=data_update)
    return result

@router.delete("/delete_user")
async def delete_by_cif(response: Response,cif:str):
    result = Fira.delete_by_cif(cif=cif)
    return result