from django.urls import path
from mywatchlist.views import show_mywatchlist, show_mywatchlist_html, show_mywatchlist_json, show_mywatchlist_xml

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist_html, name='show_mywatchlist_html'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
]