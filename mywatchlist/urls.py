from django.urls import path
from mywatchlist.views import show_mywatchlist

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
]