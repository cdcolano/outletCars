from django.urls import path

from proyectos.mysite.myapp.models import Trabajador

from . import views

urlpatterns = [
    # myApp/
    path('', views.index, name ='index'),
    # myApp/[nombre_empresa]
    path('<str:nombre_empresa>', views.nombreEmpresa, name ='empresas_por_nombre'),
    # myApp/empresa/[id_empresa]
    path('empresas/<int:id_empresa>', views.idEmpresa, name ='id'),


    path(views.EmpresaDetailView.as_view(), name="detail_view_lista"),
    path(views.EmpresaListView.as_view(), name="empresa_list_view")
    

]
