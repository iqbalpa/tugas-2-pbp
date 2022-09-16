# import httpresponse
from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.
def show_mywatchlist(request):
    mywatchlist = MyWatchList.objects.all()
    context = {
        "watchlist": mywatchlist
    }
    return render(request, 'mywatchlist.html', context)