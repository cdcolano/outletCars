from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    

    path('categorias',views.CategoriaListView.as_view(), name="categoria_list_view"),
    path('categorias/<int:id_categoria>',views.CategoríaDetailView.as_view(), name="detalle_categoria"),
    path('coches',views.CocheListView.as_view(), name="coche_list_view"),
    path('coches/<str:matricula>',views.CocheDetailView.as_view(), name="detalle_coche"),
    path('marcas',views.ListaMarcasListView.as_view(), name="marca_list_view"),
    path('marcas/<int:id_marca>',views.MarcaDetailView.as_view(), name= "detalle_marca")



]