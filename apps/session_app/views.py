from django.shortcuts import render, HttpResponse, redirect
import datetime
# https://stackoverflow.com/questions/5110352/how-do-i-display-current-time-using-python-django

def index(response):
    context = { 'now': datetime.datetime.now()}
    print("-"*50)
    print(context)
    print("-"*50)
    return render(response , "session_app/index.html", context)

def create(request):
    return redirect("/")
