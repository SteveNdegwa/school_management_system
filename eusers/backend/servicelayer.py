from eusers.models import Guardian, Student, Teacher, Admin
from utils.servicebase import ServiceBase


class GuardianService(ServiceBase):
    manager = Guardian.objects


class StudentService(ServiceBase):
    manager = Student.objects


class TeacherService(ServiceBase):
    manager = Teacher.objects


class AdminService(ServiceBase):
    manager = Admin.objects