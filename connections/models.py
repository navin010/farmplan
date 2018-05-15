from django.db import models
from accounts.models import FarmUser
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.


#Client Table
class ClientTable(models.Model):
    #user = models.ForeignKey(FarmUser, on_delete=models.CASCADE)
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
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        unique_together = (('user','message_type','direction','client'))    #prevent duplicates
        ordering  = ('client', 'direction')                                 #order by client then direction

    def _get_unique_slug(self):                                             #increment slug value suffix, as cannot use id value, id value is set after being stored not before
        slug = slugify(self.user)
        unique_slug = slug
        num = 1
        while ConnectionTable.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug


    def save(self, *args, **kwargs):
        self.slug = self._get_unique_slug()
        super(ConnectionTable, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('connections:modify_connection', args=[self.slug])  #setup url for object


    def __str__(self):          #diplay object as string
        return '%s' % (self.user)