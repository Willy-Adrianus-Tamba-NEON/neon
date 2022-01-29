from datetime import date
from pydantic import BaseModel
from typing import Optional, List

class Loans(BaseModel):
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
    dob: str = None
    gender: str = None
    marital_status: str = None
    income: int = None
    phone: str = None
    email: str = None
    isphoneverified: int = None
    isemailverified: int = None
    createdate: str = None
    updatedate: str = None
    source: str = None

class ResponseLoans(BaseModel):
    loan_list: List[Loans]
