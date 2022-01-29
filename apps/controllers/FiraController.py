from sqlalchemy import null
from apps.helper import Log
from apps.schemas import BaseResponse
from apps.helper.ConfigHelper import encoder_app
from apps.schemas.SchemaFira import ResponseLoans, Loans
from main import PARAMS
from apps.models.LoanModel import Loan

SALT = PARAMS.SALT.salt


class ControllerFira(object):
    @classmethod
    def get_user_by_cif(cls,cif):
        result = BaseResponse()
        result.status = 400

        if cif is not None:
            data = Loan.where('cif',cif).get().serialize()
            result.status = 200
            result.message = "Success"
            result.data = data
        
        else:
            m = "cif not found!"
            Log.error(m)
            result.status = 404
            result.message = str(m)

        return result

    @classmethod
    def insert_new_data(cls, input_data=None):
        result = BaseResponse()
        result.status = 400
        input_data = Loans(**input_data)

        try:
            if input_data.loanid is not None and input_data.loanid not in input_data.lists("loanid"):
                Loan.insert(input_data)
                result.status = 200
                result.message = "Input Data Success"
                Log.info(result.message)
            else:
                result.status = 404
                result.message = "We can't insert your data because loanid is empty"
                Log.info(result.message)
        except:
            e = "Error"
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result
    
    @classmethod
    def edit_by_cif(cls, cif=None, data_update=None):
        result = BaseResponse()
        result.status = 400

        try:
            if cif is not None and cif in Loan.lists("cif"):
                Loan.where('cif','=',cif).update(data_update)
                data = Loan.where('cif','=',cif).get().serialize()
                result.status = 200
                result.message = "Data Updated"
                result.data = data
            elif cif not in Loan.lists("cif"):
                result.status = 404
                result.message = "CIF Not Found"
            else:
                result.status = 400
                result.message = "Input is Empty"
                Log.info(result.message)
        except:
            e = "Error"
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def delete_by_cif(cls, cif=None):
        result = BaseResponse()
        result.status = 400

        try:
            if cif is not None and cif in Loan.lists("cif"):
                Loan.where('cif', '=', cif).delete()
                result.status = 200
                result.message = "Data Deleted"        
            elif cif not in Loan.lists("cif"):
                result.status = 404
                result.message = "CIF Not Found"
            else:
                result.status = 400
                result.message = "Input is Empty"
                Log.info(result.message)
        except:
            e = "Error"
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result