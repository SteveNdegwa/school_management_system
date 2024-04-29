from base.models import State, Role, RolePermission, Permission
from utils.servicebase import ServiceBase


class StateService(ServiceBase):
    manager = State.objects


class RoleService(ServiceBase):
    manager = Role.objects


class PermissionService(ServiceBase):
    manager = Permission.objects


class RolePermissionService(ServiceBase):
    manager = RolePermission.objects
