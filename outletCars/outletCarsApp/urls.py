from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    

    path('listaCategorias/',views.CategoriaListView.as_view(), name="categoria_list_view"),
    path('categoria/<int:id_categoria>',views.CategoríaDetailView.as_view(), name="detalle_categoria"),
    path('listaCoches/',views.CocheListView.as_view(), name="coche_list_view"),
    path('coche/<str:matricula>',views.CocheDetailView.as_view(), name="detalle_coche"),
    path('listaMarcas/',views.ListaMarcasListView.as_view(), name="marca_list_view"),
    path('marca/<int:marca_id>',views.MarcaDetailView.as_view(), name= "detalle_marca")



]