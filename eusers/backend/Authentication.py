import logging
import random

from django.http import JsonResponse
from django.db.models import Q

from base.models import Role
from eusers.backend.servicelayer import EUserService
from utils.TransactionLogBase import TransactionLogBase
from utils.get_request_data import get_request_data

lgr = logging.getLogger(__name__)


def generate_password(length=6):
    """
 This function generates the random passwords for users.
 @param length: The number of characters the password should have. Defaults to 6.
 @type length: int
 @return: The generated password.
 @rtype: str
 """
    # noinspection SpellCheckingInspection
    import string
    groups = [
        string.ascii_uppercase.replace('O', '').replace('I', ''), string.digits,
        string.ascii_lowercase.replace('o', '').replace('i', '').replace('l', ''), '!#%&+:;?@[]_{}']
    cln = [random.choice(groups[n]) for n in range(4)]
    for m in range(length):
        if len(cln) >= length:
            break
        cln.append(random.choice(groups[int(random.choice('0123'))]))
    random.shuffle(cln)
    return ''.join(cln)


class Authentication(TransactionLogBase):
    def register_user(self, request):
        transaction = None
        try:
            transaction = self.log_transaction(transaction_type='RegisterUser', request=request)
            if not transaction:
                return JsonResponse({"code": "999.999.000", 'message': 'Error creating transaction'})
            data = get_request_data(request)
            id_no = data.get('id_no', '')
            first_name = data.get('first_name', '')
            last_name = data.get('last_name', '')
            email = data.get('email', '')
            phone_number = data.get('phone_number', '')
            other_phone_number = data.get('other_phone_number', '')
            if not first_name:
                lgr.exception("First name not provided")
                response = {"code": "300.000.001", "message": "Please provide your first name"}
                self.mark_transaction_failed(transaction, response)
                return JsonResponse(response)
            if not last_name:
                lgr.exception("Last name not provided")
                response = {"code": "300.000.002", "message": "Please provide your last name"}
                self.mark_transaction_failed(transaction, response)
                return JsonResponse(response)
            if not id_no:
                lgr.exception("Id no not provided")
                response = {"code": "300.000.003", "message": "Please provide your Id no"}
                self.mark_transaction_failed(transaction, response)
                return JsonResponse(response)
            if not email:
                lgr.exception("Email not provided")
                response = {"code": "300.000.004", "message": "Please provide an email"}
                self.mark_transaction_failed(transaction, response)
                return JsonResponse(response)
            if not phone_number:
                lgr.exception("Phone number not provided")
                response = {"code": "300.000.005", "message": "Please provide your phone number"}
                self.mark_transaction_failed(transaction, response)
                return JsonResponse(response)

            if EUserService().get(id_no=id_no, state__name="Active"):
                lgr.exception("Id no already exists")
                response = {"code": "300.000.006", "message": "Id no already exists"}
                self.mark_transaction_failed(transaction, response)
                return JsonResponse(response)
            if EUserService().get(email=email, state__name="Active"):
                lgr.exception("Email already exists")
                response = {"code": "300.000.007", "message": "Email already exists"}
                self.mark_transaction_failed(transaction, response)
                return JsonResponse(response)
            if EUserService().get(Q(phone_number=phone_number) | Q(other_phone_number=phone_number),
                                  state__name="Active"):
                lgr.exception("Phone number already exists")
                response = {"code": "300.000.008", "message": "Phone number already exists"}
                self.mark_transaction_failed(transaction, response)
                return JsonResponse(response)
            if EUserService().get(Q(phone_number=other_phone_number) | Q(other_phone_number=other_phone_number),
                                  state__name="Active"):
                lgr.exception("Other phone number already exists")
                response = {"code": "300.000.009", "message": "Other phone number already exists"}
                self.mark_transaction_failed(transaction, response)
                return JsonResponse(response)

            is_admin = data.get('is_admin', False)

            k = {
                "first_name": first_name,
                "last_name": last_name,
                "other_name": data.get('other_name', ''),
                "dob": data.get('dob', ''),
                "id_no": id_no,
                "phone_number": phone_number,
                "other_phone_number": other_phone_number,
                "email": data.get('email', ''),
                "role": Role.default_admin() if is_admin else Role.default_teacher()
            }
            user = EUserService().create(**k)
            if not user:
                lgr.exception('Error creating user: %s', data.get('first_name'))
                response = {"code": "300.000.001", "message": "Error creating user"}
                self.mark_transaction_failed(transaction, response)
                return JsonResponse(response)
            password = generate_password()
            user.set_password(password)
            response = {"code": "100.000.000", "message": "User created successfully"}
            self.complete_transaction(transaction, response)
            return JsonResponse(response)

        except Exception as e:
            self.mark_transaction_failed(transaction)
            lgr.exception('Register user Exception: %s', e)
