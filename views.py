from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title' : 'HomePage',
        'footer' : ''
    }
    return render(request, 'fort/index.html', context)