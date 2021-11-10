from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    

    #path('listaCategorias',views.CategoriaListView.as_view(), name="categoria_list_view"),
    #path('categoria/<int: categoria_id>',views.CategoríaDetailView.as_view(), name="categoria_detail_view"),
    #path('listaCoches',views.CocheListView.as_view(), name="coche_list_view"),
    #path('coche/<str : matricula>',views.CocheDetailView.as_view(), name="coche_detail_view"),
    #path('listaMarcas',views.ListaMarcasListView.as_view(), name="marca_list_view"),
    #path('marca/marca_id',views.MarcaDetailView.as_view(), name= "marca_detail_view")



]