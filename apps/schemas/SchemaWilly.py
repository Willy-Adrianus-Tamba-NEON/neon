from datetime import date
import email
from pydantic import BaseModel
from typing import Optional, List

class RequestMyLoan(BaseModel):
    loanid: str = None

class myLoan(BaseModel):
    loanid: str = None
    loan_type: int = None
    loan_status: int = None
    loan_amount: int  = None
    loan_tenure: int  = None
    interest: int = None
    cif: str  = None
    idno: str = None
    fname: str = None
    lname: str = None
    dob: date = None
    gender: str = None
    marital_status: str = None
    income: int = None
    phone: str = None
    email: str = None
    isphoneverified: int = None
    isemailverified: int = None
    createdate: date = None
    updatedate: date = None
    risky: int = None
    source: str = None

class ResponseMyLoan(BaseModel):
    loanid_list: List[myLoan]

# Insert User
class RequestInsertUser(BaseModel):
    loanid: str = None
    loan_type: int = None
    loan_status: int = None
    loan_amount: int  = None
    loan_tenure: int  = None
    interest: int = None
    cif: str  = None
    idno: str = None
    fname: str = None
    lname: str = None
    dob: date = None
    gender: str = None
    marital_status: str = None
    income: int = None
    phone: str = None
    email: str = None
    isphoneverified: int = None
    isemailverified: int = None
    createdate: date = None
    updatedate: date = None
    source: str = None

class InsertUser(BaseModel):
    loanid: str = None
    loan_type: int = None
    loan_status: int = None
    loan_amount: int  = None
    loan_tenure: int  = None
    interest: int = None
    cif: str  = None
    idno: str = None
    fname: str = None
    lname: str = None
    dob: date = None
    gender: str = None
    marital_status: str = None
    income: int = None
    phone: str = None
    email: str = None
    isphoneverified: int = None
    isemailverified: int = None
    createdate: date = None
    updatedate: date = None
    source: str = None

class ResponseInsertUser(BaseModel):
    user_list: List[InsertUser]


# Risky User
class RequestRiskyUser(BaseModel):
    risky: int = None

class RiskyUser(BaseModel):
    risky: int = None
    loanid: str = None
    loan_type: int = None
    loan_status: int = None
    loan_amount: int  = None
    loan_tenure: int  = None
    interest: int = None
    cif: str  = None
    idno: str = None
    fname: str = None
    lname: str = None
    dob: date = None
    gender: str = None
    marital_status: str = None
    income: int = None
    phone: str = None
    email: str = None
    createdate: date = None
    updatedate: date = None
    source: str = None

class ResponseRiskyUser(BaseModel):
    risky_list: List[RiskyUser]


# Put
class RequestEditUser(BaseModel):
    fname: str = None
    lname: str = None
    gender: str = None
    marital_status: str = None

