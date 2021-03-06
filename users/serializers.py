from rest_framework import serializers

from .models import Users, Blogs, Admins, Comments


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('rollno','name', 'signup_date','lastlogin_date','reported_users','password','block_status')

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogs
        fields = ('sno','rollno','name','post_date','post_title','post_content','reported_user')

class AdminsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admins
        fields = ('rollno','name','lastlogin','password')

class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ('comments_id','rollno','name','comment_body','comments_date','post_id')
