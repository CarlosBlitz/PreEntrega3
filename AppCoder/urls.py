from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path('medicos/', medico, name="Medicos"),
    path('pacientes/', paciente, name="Pacientes"),
    path('turnos/', turno, name="Turnos"),
    path('turnoFormulario/', turnoFormulario, name="formularioTurno"),
    path('turnoBusqueda/', turnoBusqueda, name="turnoBusqueda"),
    path('resultados/', resultados, name="resultadosBusqueda"),
]