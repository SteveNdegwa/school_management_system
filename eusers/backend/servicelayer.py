from eusers.models import Guardian, Student, EUser, StudentPassword, EUserPassword
from utils.ServiceBase import ServiceBase


class EUserService(ServiceBase):
    manager = EUser.objects


class EUserPasswordService(ServiceBase):
    manager = EUserPassword.objects


class StudentService(ServiceBase):
    manager = Student.objects


class StudentPasswordService(ServiceBase):
    manager = StudentPassword.objects


class GuardianService(ServiceBase):
    manager = Guardian.objects