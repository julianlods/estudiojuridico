from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'estudiojuridico/home.html')

def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        telefono = request.POST.get("telefono")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        return HttpResponse(f"Gracias {nombre}, hemos recibido tu mensaje.")

    return render(request, 'estudiojuridico/contacto.html')

def servicios(request):
    return render(request, 'estudiojuridico/servicios.html')

def quienes_somos(request):
    return render(request, 'estudiojuridico/quienes_somos.html')

