from django.db.models.query import QuerySet
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Coche, Marca, Categoría, Motor

def index(request):
    return HttpResponse("Hello, world!")

# Create your views here.

#Lista de coches de una marca
class ListaMarcasListView(ListView):
    model=Marca 
    context_object_name='marcas_list'
   
class MarcaDetailView(DetailView):
    model=Marca
   # pk_url_kwarg = "id"
   # pk_field = "id"
    context_object_name='marca'
    #template_name='marca_detail.html'
     #marca.coche_set.all

class vistaInicialListView(ListView):
    model=Marca
    context_object_name='marcas_list'
    template_name='outletCarsApp/vista_inicio.html'
#    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
#        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
#        context['coche'] = Coche.objects.order_by('precio')[:1].get()
#        return context


    

class CocheListView(ListView):
    model=Coche
    queryset= Coche.objects.order_by('precio')
    context_object_name='coches_list'

class CocheDetailView(DetailView):
    model=Coche
    slug_url_kwarg = "matricula"
    slug_field = "matricula"
    #for categoria in coche.categoria 


class AjaxView(DetailView):
    model=Coche
  #  slug_url_kwarg = "matricula"
  #  slug_field = "matricula"
    template_name='outletCarsApp/ajax.html'
    #for categoria in coche.categoria 

class CategoriaListView(ListView):
    model=Categoría
    context_object_name='categorias_list'
     #for coche in categoria.coche_set.all()

class CategoríaDetailView(DetailView):
    model=Categoría
    #slug_url_kwarg = "id"
   # slug_field = "id"
    context_object_name='categoria'

class MotorDetailView(DetailView):
    model= Motor
    context_object_name='motor'