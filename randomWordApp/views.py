from django.shortcuts import render, redirect
#from django.utils.crypto import get_random_string

# Create your views here.

def randomWord(request):
   # request.session['word'] = get_random_string(length=14)
    return render(request, 'index.html')
