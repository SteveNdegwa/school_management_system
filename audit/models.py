from django.db import models

from base.models import State, BaseModel, GenericBaseModel
from eusers.models import EUser


# Create your models here.


class TransactionType(GenericBaseModel):
    state = models.ForeignKey(State, default=State.default_state, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transaction(BaseModel):
    euser = models.ForeignKey(EUser, null=True, blank=True, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    source_ip = models.CharField(max_length=100, null=True, blank=True)
    request_data = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    notification_response = models.TextField(null=True, blank=True)
    successful = models.BooleanField(default=False)
    state = models.ForeignKey(State, default=State.default_state, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.euser, self.transaction_type)
