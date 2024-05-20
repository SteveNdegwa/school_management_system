from audit.models import TransactionType, Transaction
from utils.ServiceBase import ServiceBase


class TransactionTypeService(ServiceBase):
    manager = TransactionType.objects


class TransactionService(ServiceBase):
    manager = Transaction.objects