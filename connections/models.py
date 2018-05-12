from django.db import models
from accounts.models import FarmUser

# Create your models here.

#Client Table
class ClientTable(models.Model):
    client_id = models.CharField(max_length=50, default='')
    client_name = models.CharField(max_length=50, default='')
    f4f_code = models.CharField(max_length=50, default='')

    def __str__(self):          #diplay object as string
        return self.client_name


#Connection Table
class ConnectionTable(models.Model):
    user = models.ForeignKey(FarmUser, on_delete=models.CASCADE)
    message_type = models.CharField(max_length=50, default='')
    direction = models.CharField(max_length=50, default='')
    client = models.ForeignKey(ClientTable, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='awaiting approval')

    def __str__(self):          #diplay object as string
        return '%s' % (self.user.business_name)