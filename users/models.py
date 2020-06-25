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
    rollno = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='rollno')
    name = models.CharField(max_length=60)
    post_date = models.DateTimeField()
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=400)
    reported_user = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-post_date']
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

class Comments(models.Model):
    comments_id = models.IntegerField(primary_key=True)
    rollno = models.IntegerField()
    name = models.CharField(max_length=60)
    comment_body = models.CharField(max_length=400)
    comments_date = models.DateTimeField()
    post = models.ForeignKey(Blogs, on_delete=models.CASCADE,related_name='comments')
    active = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'comments'

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Comment(models.Model):
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)