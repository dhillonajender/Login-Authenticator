from django.db import models

# Create your models here.
class Usertable(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

# by default, it will be in database as authentication_usertable(i.e app_modelname)
#but to override the database default name we can use the below meta class
class Meta:
    db_table = 'Usertable'