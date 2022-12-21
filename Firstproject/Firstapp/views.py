from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    ss = '''<center>
        <hr/>
        <h2 Style='colour:Blue;'>
            HELLO USER,WELCOME TO DJANGO....!
        </h2>
        <hr/>
        </center>''' 
    return HttpResponse(ss); 