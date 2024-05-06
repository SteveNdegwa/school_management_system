from django.db import models
from django.db.models import Q
import bcrypt

from base.models import BaseModel, State, Role
from eusers.backend.servicelayer import EUserPasswordService, StudentPasswordService


# Create your models here.

class EUserPassword(BaseModel):
    euser = models.ForeignKey("EUser", blank=True, null=True, on_delete=models.CASCADE)
    password = models.CharField(max_length=255, blank=True, null=True)


class StudentPassword(BaseModel):
    student = models.ForeignKey("Student", blank=True, null=True, on_delete=models.CASCADE)
    password = models.CharField(max_length=255, blank=True, null=True)


class BaseUser(BaseModel):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    other_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    state = models.ForeignKey(State, default=State.default_state, on_delete=models.CASCADE)

    class Meta:
        abstract: True


class AbstractUser(BaseUser):
    id_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    other_phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        abstract: True


class EUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s", (self.first_name, self.last_name, self.other_name)

    def set_password(self, password):
        try:
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            password_inst = EUserPasswordService().create(euser=self, password=hashed_password)
            if password_inst:
                EUserPasswordService().filter(~Q(id=password_inst.id), euser=self, state__name='Active').update(
                    state=State.disabled_state())
                return True
        except Exception:
            pass
        return False

    def check_password(self, password):
        try:
            password_inst = EUserPasswordService().get(euser=self, state__name="Active")
            if bcrypt.checkpw(password, password_inst.password):
                return True
        except Exception:
            pass
        return False


class Guardian(AbstractUser):

    def __str__(self):
        return "%s %s %s", (self.first_name, self.last_name, self.other_name)


class Student(BaseUser):
    admission_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    guardian = models.ForeignKey(Guardian, null=True, blank=True, related_name='guardian', on_delete=models.CASCADE)
    other_guardian = models.ForeignKey(Guardian, null=True, blank=True, related_name='other_guardian',
                                       on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s", (self.first_name, self.last_name, self.other_name)

    def set_password(self, password):
        try:
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            password_inst = StudentPasswordService().create(euser=self, password=hashed_password)
            if password_inst:
                StudentPasswordService().filter(~Q(id=password_inst.id), euser=self, state__name='Active').update(
                    state=State.disabled_state())
                return True
        except Exception:
            pass
        return False

    def check_password(self, password):
        try:
            password_inst = StudentPasswordService().get(euser=self, state__name="Active")
            if bcrypt.checkpw(password, password_inst.password):
                return True
        except Exception:
            pass
        return False
