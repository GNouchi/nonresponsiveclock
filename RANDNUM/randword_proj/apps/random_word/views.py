from django.shortcuts import render, redirect, HttpResponse
from  django.utils.crypto import get_random_string 

def index(request):
    if 'num' not in request.session:
        request.session['num'] = 1
    content = {
        'randomword':get_random_string(length=14),
        'num': request.session['num']
    }
    return render(request, "random_word/index.html", content )

def random_word(request):
# intentionally does not increment on self-direct to /random_word
    if request.method == 'POST':
        request.session['num'] += 1 
    return redirect ('/')

def reset(request):
    if 'num' in request.session:
        del request.session['num']
    return redirect ('/')
