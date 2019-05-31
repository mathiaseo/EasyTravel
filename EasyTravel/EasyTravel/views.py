from django.shortcuts import render
from django.http import HttpResponse

#Post = {('id':4, 'nom':'Leonel')}

def index(request):
    return render(request, 'index.html', )#{{Post}} )

def alter(request):
    return render(request, 'alter.html', )#{{Post}} )