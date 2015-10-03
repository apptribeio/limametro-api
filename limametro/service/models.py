from django.db import models

class Service(models.Model):
    code = models.CharField(db_index = True, unique = True, max_length = 32)
    name = models.CharField(max_length = 50)
    photo = models.TextField()
    description = models.TextField()
    status = models.BooleanField()
    '''Unicode for interactive prompt'''
    def __unicode__(self):
        return self.name
    '''Meta class for table definition'''
    class Meta:
        db_table = 'limametro_service'