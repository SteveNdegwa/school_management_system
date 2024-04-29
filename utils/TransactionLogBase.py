from django.db import transaction

from base.backend.servicelayer import StateService, TransactionTypeService, TransactionService
from utils.get_request_data import get_request_data
import logging

lgr = logging.getLogger(__name__)


class TransactionLogBase(object):

    @staticmethod
    def log_transaction(transaction_type, **kwargs):
        try:
            with transaction.atomic():
                transaction_type = TransactionTypeService().get(name=transaction_type)
                return TransactionService().create(transaction_type=transaction_type, **kwargs)
        except Exception as e:
            lgr.exception('log_transaction Exception: %s', e)
        return None

