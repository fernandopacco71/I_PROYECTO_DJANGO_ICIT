from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'file/home.html')

def contactos(request):
    return render(request, 'file/contactos.html')

def nosotros(request):
    return render(request, 'file/nosotros.html')

def servicios(request):
    return render(request, 'file/servicios.html')
