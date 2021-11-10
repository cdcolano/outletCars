from django.urls import path


from . import views

urlpatterns = [
    # myApp/
    path('', views.index, name ='index'),
    # myApp/[nombre_empresa]
    path('<str:nombre_empresa>', views.nombreEmpresa, name ='empresas_por_nombre'),
    # myApp/empresa/[id_empresa]
    path('empresas/<int:id_empresa>', views.idEmpresa, name ='id'),

    

    path(views.CategoriaListView.as_view(), name="categoria_list_view"),
    path(views.CategoríaDetailView.as_view(), name="categoria_detail_view"),
    path(views.CocheListView.as_view(), name="coche_list_view"),
    path(views.CocheDetailView.as_view(), name="coche_detail_view"),
    path(views.ListaMarcasListView.as_view(), name="marca_list_view"),
    path(views.MarcaDetailView.as_view(), name= "marca_detail_view")



]