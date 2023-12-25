from django.shortcuts import render
import pyjokes

def index(request):
    return render(request, 'index.html')

def joke(request):
    chuck_joke = pyjokes.get_joke(category='chuck')
    context = {'chuck_joke': chuck_joke}  # Assigning chuck_joke to a key in the context dictionary
    return render(request, 'index.html', context)
