from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print('hello django')

    return render(request,'./index.html')


def password(request):

    return render(request,'./password.html',{'password':'1234568'})








