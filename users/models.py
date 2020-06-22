from django.db import models

# Create your models here.
class Users(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=60)
    signup_date = models.DateTimeField(auto_now_add=True)
    lastlogin_date = models.DateTimeField(auto_now=True)
    reported_users = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=40)
    block_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

class Blogs(models.Model):
    sno = models.AutoField(primary_key=True)
    rollno = models.ForeignKey('Users', models.DO_NOTHING, db_column='rollno')
    name = models.CharField(max_length=60)
    post_date = models.DateTimeField()
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=400)
    reported_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blogs'

class Admins(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    lastlogin = models.DateTimeField()
    password = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'admins'
