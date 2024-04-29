from django.db import models

from base.models import BaseModel, State, Role


# Create your models here.

class EUser(BaseModel):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    other_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    state = models.ForeignKey(State, default=State.default_state, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class AbstractEUser(EUser):
    id_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    other_phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        abstract: True


class Guardian(AbstractEUser):

    def __str__(self):
        return "%s %s %s", (self.first_name, self.last_name, self.other_name)


class Student(EUser):
    admission_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    guardian = models.ForeignKey(Guardian, null=True, blank=True, related_name='guardian', on_delete=models.CASCADE)
    other_guardian = models.ForeignKey(Guardian, null=True, blank=True, related_name='other_guardian',
                                       on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s", (self.first_name, self.last_name, self.other_name)


class Teacher(AbstractEUser):
    tsc_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s", (self.first_name, self.last_name, self.other_name)


class Admin(AbstractEUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s", (self.first_name, self.last_name, self.other_name)
