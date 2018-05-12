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
    MESSAGE_CHOICES = (
        ('movement', 'movement'),
        ('execution', 'execution'),
        ('financial', 'financial'),
    )

    DIRECTION_CHOICES = (
        ('to partner', 'to partner'),
        ('from partner', 'from partner'),
    )

    STATUS_CHOICES = (
        ('awaiting approval', 'awaiting approval'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    )


    user = models.ForeignKey(FarmUser, on_delete=models.CASCADE)
    message_type = models.CharField(max_length=50, choices=MESSAGE_CHOICES,default='')
    direction = models.CharField(max_length=50, choices=DIRECTION_CHOICES, default='')
    client = models.ForeignKey(ClientTable, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='awaiting approval')


    class Meta:
        unique_together = (('user','message_type','direction','client'))    #prevent duplicates


    def __str__(self):          #diplay object as string
        return '%s' % (self.user)