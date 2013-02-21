from django.shortcuts import render

def main(request):
    return render(request, 'main.djhtml')

def contact(request):
    return render(request, 'contact.djhtml')

