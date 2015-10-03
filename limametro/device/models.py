from django.db import models
from limametro.user.models import User

class Device(models.Model):
    user = models.ForeignKey(User)
    device = models.CharField(max_length = 40)
    token = models.CharField(max_length = 40)
    registered = models.DateTimeField()
    status = models.BooleanField()
    '''Unicode for interactive prompt'''
    def __unicode__(self):
        return self.device
    '''Meta class for table definition'''
    class Meta:
        db_table = 'limametro_device'