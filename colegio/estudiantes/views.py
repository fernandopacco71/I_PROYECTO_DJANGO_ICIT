from django.shortcuts import render


def home(request):
    proyecto = " - Colegio CIMAC-ICIT"
    cxt={
        'proyecto':proyecto,
    }
    return render(request, 'file/home.html',cxt)

def contactos(request):
    proyecto = " - Colegio CIMAC-ICIT"
    cxt={
        'proyecto':proyecto,
    }
    return render(request, 'file/contactos.html',cxt)

def nosotros(request):
    proyecto = " - Colegio CIMAC-ICIT"
    cxt={
        'proyecto':proyecto,
    }
    return render(request, 'file/nosotros.html',cxt)

def servicios(request):
    proyecto = " - Colegio CIMAC-ICIT"
    cxt={
        'proyecto':proyecto,
    }
    return render(request, 'file/servicios.html',cxt)
