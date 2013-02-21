from django.shortcuts import render
from django.conf import settings

def main(request):
    return render(request, 'main.djhtml')

def contact(request):
    return render(request, 'contact.djhtml', { 'NAVERMAPKEY': settings.NAVERMAPKEY })

