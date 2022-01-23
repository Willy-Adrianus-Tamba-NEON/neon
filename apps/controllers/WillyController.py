from apps.helper import Log
from apps.schemas import BaseResponse
from apps.helper.ConfigHelper import encoder_app
from apps.schemas.SchemaWilly import RequestEditUser, RequestMyLoan, ResponseMyLoan, RequestRiskyUser, ResponseRiskyUser, RequestInsertUser, ResponseInsertUser
from main import PARAMS
from apps.models.LoanModel import Loan

SALT = PARAMS.SALT.salt


class ControllerWilly(object):
    @classmethod
    def insert_user(cls, input_data=None):
        input_data = RequestInsertUser(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.loanid is not None:
                Loan.insert(input_data)
                data = Loan.where('loanid', '=', input_data.loanid).get().serialize()
                result.status = 200
                result.message = "Input Data Success"
                result.data = ResponseInsertUser(**{'user_list': data})
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
    def get_risky_user(cls, risky):
        result = BaseResponse()
        result.status = 400

        try:
            if risky is not None:
                if risky in Loan.lists("risky"):
                    data = Loan.where('risky', '=', risky).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseRiskyUser(**{"risky_list": data})
                    Log.info(result.message)
                elif risky not in range (Loan.min('risky'), Loan.max('risky')+1):
                    result.status = 404
                    result.message = f"No loan status above {Loan.max('risky')} or below {Loan.min('risky')}" 
                else:
                    result.status = 404
                    result.message = "not found"

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def delete_user_by_loanid(cls, loanid=None):
        result = BaseResponse()
        result.status = 400

        try:
            if loanid is not None:
                if loanid in Loan.lists("loanid"):
                    data = Loan.where('loanid', '=', loanid)
                    view = data.get().serialize()
                    data.delete()
                    result.status = 200
                    result.message = f"Success Delete data by loanid: {loanid}"
                    result.data = ResponseMyLoan(**{'loanid_list': view})
                    Log.info(result.message)
                else:
                    result.status = 404
                    result.message = "loanid not found"
            else:
                result.status = 400
                result.message = "There's no input"
                Log.info(result.message)
        except:
            m = "Error"
            Log.error(m)
            result.status = 400
            result.message = str(m)

        return result


    @classmethod
    def edit_user_by_loanid(cls, loanid=None, input_data=None):
        input_data = RequestEditUser(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if loanid is not None:
                if loanid in Loan.lists("loanid"):
                    Loan.where('loanid', loanid).update(input_data)
                    data = Loan.where('loanid', loanid).get().serialize()
                    result.status = 200
                    result.message = f"Updated user for: {loanid}"
                    result.data = ResponseMyLoan(**{'user_list': data})
                    Log.info(result.message)
                else:
                    result.status = 404
                    result.message = "loanid not found"
            else:
                result.status = 400
                result.message = "none input"
                Log.info(result.message)
        except:
            m = "Error"
            Log.error(m)
            result.status = 400
            result.message = str(m)

        return result

#  @classmethod
#     def update_demography_data(cls, id_no=None, update_data=None):
#         update_data = RequestUpdateData(**update_data)
#         result = BaseResponse()
#         result.status = 400

#         try:
#             if id_no is not None:
#                 if id_no in Loan.lists("idno"):
#                     Loan.where('idno', id_no).update(update_data)
#                     data = Loan.where('idno', id_no).get().serialize()
#                     result.status = 200
#                     result.message = f"Update phone number by id no: {id_no}"
#                     result.data = ResponseLoanStatus(**{'status_list': data})
#                     Log.info(result.message)
#                 else:
#                     result.status = 404
#                     result.message = "idno not found"
#             else:
#                 result.status = 400
#                 result.message = "There's no input"
#                 Log.info(result.message)
#         except:
#             m = "Error"
#             Log.error(m)
#             result.status = 400
#             result.message = str(m)

#         return result