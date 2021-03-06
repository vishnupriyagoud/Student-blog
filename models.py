# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime


class Blog(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=60)
    post_date = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=400)
    reported_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog'


class Users(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=60)
    signup_date = models.DateTimeField(auto_now_add=True)
    lastlogin_date = models.DateTimeField(auto_now=True)
    reported_users = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'users'
