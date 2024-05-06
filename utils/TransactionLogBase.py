from django.db import transaction

from base.backend.servicelayer import StateService, TransactionTypeService, TransactionService
from eusers.backend.servicelayer import EUserService
from utils.get_request_data import get_request_data
import logging

lgr = logging.getLogger(__name__)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class TransactionLogBase(object):

    @staticmethod
    def log_transaction(**kwargs):
        try:
            request_data = get_request_data(kwargs.get("request"))
            k = {
                "euser": EUserService().get(id=request_data.get('user_id')),
                "transaction_type": TransactionTypeService().get(name=kwargs.get("transaction_type")),
                "request_data": request_data,
                "source_ip": get_client_ip(kwargs.get('request')),
            }
            return TransactionService().create(**k)
        except Exception as e:
            lgr.exception('log_transaction Exception: %s', e)
        return None

    @staticmethod
    def mark_transaction_failed(trx, response):
        try:
            return TransactionService().update(trx.id, response=response, state=StateService().get(name='Failed'))
        except Exception as e:
            lgr.exception('Mark transaction as failed Exception: %s', e)
        return None

    @staticmethod
    def complete_transaction(trx, response):
        try:
            return TransactionService().update(trx.id, response=response, successful=True,
                                               state=StateService().get(name='Completed'))
        except Exception as e:
            lgr.exception('Mark transaction as failed Exception: %s', e)
        return None
