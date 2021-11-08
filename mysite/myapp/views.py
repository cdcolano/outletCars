from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Empresa, Trabajador

def index(request):
    return HttpResponse("Hello, world!")

# Create your views here.

def nombreEmpresa(request, nombre_empresa):
    lista_empresas = get_list_or_404(Empresa, nombre = nombre_empresa)
    context = {
        'variable' : lista_empresas
    }
    render(request, 'listaEmpresas.html', context)

def idEmpresa(request, id_empresa):
    empresa = get_object_or_404(Empresa, pk = id_empresa)

class EmpresaDetailView(DetailView):
    model=Empresa

class EmpresaListView(ListView):
    model=Empresa

class EmpleadoDetailView(DetailView):
    model=Trabajador