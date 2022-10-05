from django.shortcuts import render
from django.http import HttpResponse


import random


# Create your views here.
def index(request):
    print('hello django')

    return render(request,'./index.html')


def password(request):

    chars= [chr(c) for c in range(97,123)]
    print(chars)
    # input_length=request.GET.get('input-length')
    # if input_length =='':
    #     input_length=request.GET.get('length')
        # print(input_length)
    if request.GET.get('uppercase'):
        chars+=[chr(c).upper() for c in range(97,123)]

    print(chars)

    if request.GET.get('numbers'):
        chars+=[str(c) for c in range(0,11)]
    print(chars)

    if request.GET.get('special'):
        chars+=list('@#!$%^&*')
    print(chars)

    length=eval(request.GET.get('length')) if request.GET.get('input-length')==''\
        else eval(request.GET.get('input-length'))

    password=''.join([random.choice(chars) for i in range(length)])
    print(password)
    print(length)

    return render(request,'./password.html',{'password':password})








