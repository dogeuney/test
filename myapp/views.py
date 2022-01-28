from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
import random
# Create your views here.
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ...'},
    {'id':2, 'title':'view', 'body':'View is ...'},
    {'id':3, 'title':'model', 'body':'Model is ...'}
]
def index(request):
    article='''
        <h2>Welcome</h2>
        Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)