from django.db import models

class Token(models.Model):
    name = models.CharField(max_length = 45)
    username = models.CharField(max_length = 45)
    token = models.CharField(max_length = 40)
    created = models.DateTimeField()
    status = models.BooleanField()
    '''Unicode for interactive prompt'''
    def __unicode__(self):
        return self.name
    '''Meta class for table definition'''
    class Meta:
        db_table = 'limametro_token'