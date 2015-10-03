from django.db import models
from limametro.service.models import Service

class Station(models.Model):
    code = models.CharField(db_index = True, unique = True, max_length = 32)
    name = models.CharField(max_length = 50)
    services = models.ManyToManyField(Service)
    map = models.TextField()
    address = models.CharField(max_length = 100)
    lat = models.FloatField()
    long = models.FloatField()
    open_hour = models.TimeField()
    close_hour = models.TimeField()
    status = models.BooleanField()
    '''Unicode for interactive prompt'''
    def __unicode__(self):
        return self.name
    '''Meta class for table definition'''
    class Meta:
        db_table = 'limametro_station'