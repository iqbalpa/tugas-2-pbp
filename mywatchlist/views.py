# import httpresponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_mywatchlist(request):
    return render(request, 'mywatchlist.html')