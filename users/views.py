from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.template import loader
from django.contrib import messages 
from .forms import CommentsForm
# Create your views here.
from rest_framework import viewsets
from django.db import connection
from .serializers import UsersSerializer, BlogSerializer, AdminsSerializer, CommentsSerializer
from .models import Users, Blogs, Admins, Comments
from rest_framework.decorators import api_view
import json
import requests
from datetime import datetime

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

class AdminsViewSet(viewsets.ModelViewSet):
    queryset = Admins.objects.all()
    serializer_class = AdminsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer



def index1(request):
    context = {

    }
    return render(request, 'index.html', context)


def finduser(request):
    #ret=render(request,'users/index1.html')
    if request.method == 'POST':
        username = request.POST['login'] 
        password = request.POST['password']
        user=""
        admin = Admins.objects.all()
        for user in admin:
            if username==user.name and password==user.password:
                cursor= connection.cursor()
                row=''
                user.lastlogin=datetime.now()
                user.save()
                context= {
                    'row' : cursor.execute("SELECT * FROM blogs"),
                    'blogs': cursor.fetchall()
                }
                re=render(request,'mainpage.html',context)
                return re

    return render(request,'index1.html')

 
"""def post_delete(request,pk):
    cursor= connection.cursor()
    row=''
    context= {
        'row' : cursor.execute("DELETE FROM blogs WHERE sno=pk"),
        'blogs': cursor.fetchall()
    }
    return render(request,'result1.html',context)"""

def post_delete(request, pk):
    post=Blogs.objects.get(sno=pk)
    post.delete()
    cursor= connection.cursor()
    row=''
    context= {
        'row' : cursor.execute("SELECT * FROM blogs"),
        'blogs': cursor.fetchall()
    }
    return render(request,'result.html',context)

def post_edit(request, pk):
    post=Blogs.objects.get(sno=pk)
    cursor= connection.cursor()
    row=''
    context={
        'row' : cursor.execute("SELECT * FROM blogs"),
        'blogs': cursor.fetchone()
    }
    return render(request,'result1.html',context)

def edit_post(request, pk):
    post=Blogs.objects.get(sno=pk)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content_text']
        post.post_content=content
        post.post_title=title
        post.save()
        cursor= connection.cursor()
        row=''
        context={
            'title':post.post_title,
            'content':post.post_content,
            'row' : cursor.execute("SELECT * FROM blogs"),
            'blogs': cursor.fetchall(),
        }
        
        return render(request,'result.html',context)


def post_report(request,pk):
    return HttpResponse("reported")

def post_block(request,pk):

    return HttpResponse("blocked")


def post_comment(request, slug):
    template_name = 'post_detail.html'
    post=Blogs.objects.get(sno=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form=""
    # Comment posted
    context={
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    if request.method == 'POST':
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentsForm()

    return render(request, template_name, context)







