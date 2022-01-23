from asyncio.windows_events import NULL
import json
from unittest import result
from fastapi import APIRouter, Body, Response
from apps.controllers.WillyController import ControllerWilly as loan

router = APIRouter()


@router.get("/get_risky_user/{risky}")
async def get_risky_user(response: Response, risky:int = 0):
    result = loan.get_risky_user(risky)
    response.status_code = result.status
    return result


input_insert_data = json.dumps({
    "loanid": "",
    "loan_type": None,
    "loan_status": None,
    "loan_amount": None,
    "loan_tenure": None,
    "interest": None,
    "cif": "",
    "idno": "",
    "fname": "",
    "lname": "",
    "dob": None,
    "gender": "",
    "marital_status": "",
    "income": None,
    "phone": "",
    "email": "",
    "isphoneverified": None,
    "isemailverified": None,
    "createdate": None,
    "updatedate": None,
    "source": "",
}, indent=2)
@router.post("/insert_user")
async def insert_user(response: Response, input_data=Body(..., example=input_insert_data)):
    result = loan.insert_user(input_data=input_data)
    response.status_code = result.status
    return result

edit_user_example= json.dumps({
    "fname": 'Willy',
    "lname": 'Tamba',
    "gender": "Male",
    "marital_status": "Single",
})
@router.put("/edit_user")
async def edit_user_by_loanid(response: Response, loanid: str, input_data=Body(..., example=edit_user_example)):
    result = loan.edit_user_by_loanid(loanid=loanid, update_data=input_data)
    return result


@router.delete("/delete_user")
async def delete_user_by_loanid(response: Response, loanid=None):
    result = loan.delete_user_by_loanid(loanid=loanid)
    return result
