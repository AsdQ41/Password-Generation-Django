from django.shortcuts import render
import random

def home(request):
    return render(request, 'generation/index.html')


def password(request):

    thepassword = ''

    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) 

    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()')) 
 
    if request.GET.get('numbers'):
        character.extend(list('0123456789')) 

    lenght = int(request.GET.get('length', 12))

    for x in range(lenght):
        thepassword += random.choice(character)

    return render(request, 'generation/generation.html', {'password':thepassword})

def about(request):
    return render(request, 'generation/about.html')    