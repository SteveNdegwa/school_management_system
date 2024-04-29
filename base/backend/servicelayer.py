from base.models import State, Role, RolePermission, Permission, Transaction, TransactionType
from utils.ServiceBase import ServiceBase


class StateService(ServiceBase):
    manager = State.objects


class RoleService(ServiceBase):
    manager = Role.objects


class PermissionService(ServiceBase):
    manager = Permission.objects


class RolePermissionService(ServiceBase):
    manager = RolePermission.objects


class TransactionService(ServiceBase):
    manager = Transaction.objects


class TransactionTypeService(ServiceBase):
    manager = TransactionType.objects

