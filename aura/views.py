from django.shortcuts import render
from django.conf import settings

def main(request):
    return render(request, 'main.djhtml')

def contact(request):
    return render(request, 'contact.djhtml', { 'NAVERMAPKEY': settings.NAVERMAPKEY,
                                               'GOOGLEMAPKEY': settings.GOOGLEMAPKEY})

def product(request):
    return render(request, 'product.djhtml')

def members(request):
    return render(request, 'members.djhtml')

