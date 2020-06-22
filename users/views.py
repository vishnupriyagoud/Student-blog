from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.template import loader
from django.contrib import messages 

# Create your views here.
from rest_framework import viewsets
from django.db import connection
from .serializers import UsersSerializer, BlogSerializer, AdminsSerializer
from .models import Users, Blogs, Admins
from rest_framework.decorators import api_view
import json
import requests

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

class AdminsViewSet(viewsets.ModelViewSet):
    queryset = Admins.objects.all()
    serializer_class = AdminsSerializer



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
        users = Users.objects.all()
        for user in users:
            if username==user.name and password==user.password:
                cursor= connection.cursor()
                row=''
                context= {
                    'row' : cursor.execute("SELECT * FROM blogs"),
                    'blogs': cursor.fetchall()
                }
                re=render(request,'result.html',context)
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






