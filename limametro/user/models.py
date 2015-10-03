from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 50)
    registered = models.DateTimeField()
    status = models.BooleanField()
    '''Unicode for interactive prompt'''
    def __unicode__(self):
        return self.email
    '''Meta class for table definition'''
    class Meta:
        db_table = 'limametro_user'