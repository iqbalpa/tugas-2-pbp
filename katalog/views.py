from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'data_katalog': data_katalog,
    }
    return render(request, 'katalog.html', context)