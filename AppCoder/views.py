from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import turnoFormulario
from AppCoder.models import *

# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def medico(request):
    med1 = Medico(nombre="Juan",apellido="Pérez", especialidad="Generalista")
    med1.save()

    return render(request,"AppCoder/medicos.html")

def paciente(request):
    return render(request,"AppCoder/pacientes.html")

def turno(request):
    

    return render(request,"AppCoder/turnos.html")

def turnoFormulario(request):
    
    if request.method == "POST":
        
        formulario1 = turnoFormulario(request.POST)

        if formulario1.is_valid():
            
            info = formulario1.cleaned_data
            
            turno = Turno(prestador=info["Prestador"], solicitante=info["Solicitante"], fecha=info["Fecha"])

            turno.save()

            return render(request, "AppCoder/inicio.html")
        
    else:

        formulario1 = turnoFormulario()

    return render(request, "AppCoder/turnoFormulario.html", {"form1":formulario1})

def turnoBusqueda(request):

    return render(request, "AppCoder/inicio.html")

def resultados(request):

    if request.GET["prestador"]:

        prestador = request.GET["prestador"]
        turno = Turno.objects.filter(prestador__icontains=prestador)

        return render(request, "AppCoder/inicio.html", {"prestador":prestador})
    
    else:

        respuesta = "No hay datos"

    return HttpResponse(respuesta)