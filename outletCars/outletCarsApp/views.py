from django.db.models.query import QuerySet
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Coche, Marca, Categoría

def index(request):
    return HttpResponse("Hello, world!")

# Create your views here.

#Lista de coches de una marca
class ListaMarcasListView(ListView):
    model=Marca 
    context_object_name='marcas_list'
   
class MarcaDetailView(DetailView):
    model=Marca
    slug_url_kwarg = "id"
    slug_field = "id"
    context_object_name='marca'
     #marca.coche_set.all

class vistaInicialListView(ListView):
    model=Marca
    #for coche in marca.Coche_set.all()
        #te quedas solo con el primero

class CocheListView(ListView):
    model=Coche
    queryset= Coche.objects.order_by('precio')
    context_object_name='coches_list'

class CocheDetailView(DetailView):
    model=Coche
    #for categoria in coche.categoria 

class CategoriaListView(ListView):
    model=Categoría
    context_object_name='categorias_list'
     #for coche in categoria.coche_set.all()

class CategoríaDetailView(DetailView):
    model=Categoría
