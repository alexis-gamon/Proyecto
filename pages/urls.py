from django.urls import path, include


from .views import ResultadoBusquedaListView, homeTemplateView, PeliculaListView, PeliculaTemplateView, PeliculaPageDetail, PeliculaPagesCreate, PeliculaPageUpdate, PeliculaPageDelete

urlpatterns = [

    
    path('', homeTemplateView.as_view(), name='home'),
   # path('PeliculasTerror/',PeliculasTerrorTemplateView.as_view(), name='PeliculasTerror'),

    path('pelicula/',PeliculaTemplateView.as_view(), name='pelicula'),

    path('<int:pk>/', PeliculaPageDetail.as_view(), name='pelicula_detalle'),

    path('nuevo/', PeliculaPagesCreate.as_view(), name="pelicula_nueva"),

    path('<int:pk>/editar/', PeliculaPageUpdate.as_view(), name="pelicula_editar"),

    path('<int:pk>/eliminar/', PeliculaPageDelete.as_view(), name="pelicula_eliminar"),


   # path('signup/', SignUpView.as_view(), name='signup'),
    path('', homeTemplateView.as_view(), name='home'),

    path('busquedaPeli/',ResultadoBusquedaListView.as_view(), name="resul_busqueda"),

]