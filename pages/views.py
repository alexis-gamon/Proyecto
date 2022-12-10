from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pelicula
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin##obliga a que estes logeado para poder visualizar una vista
from django.core.exceptions import PermissionDenied##valida los permisos
from django.http import HttpResponse
from django.db.models import Q



class PeliculaListView(LoginRequiredMixin, ListView):
    model = Pelicula
    template_name = 'lista_pelicula.html'
    context_object_name = 'lista_pelicula'
    login_url = 'login'

# Create your views here.
#class PeliculaTemplateView(LoginRequiredMixin, ListView):
class PeliculaTemplateView(LoginRequiredMixin, ListView):
    template_name = 'pelicula.html'
    model = Pelicula
    context_object_name = 'Todas_peliculas'
    login_url = 'login'

class homeTemplateView(TemplateView):
    template_name = 'home.html'



class PeliculaPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'pelicula_detalle.html'
    model = Pelicula
    context_object_name = 'Pelicula'
    login_url = 'login'
    permission_requerid = 'pages.suscriptor'
    


    

class PeliculaPagesCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'pelicula_nueva.html'
    model = Pelicula
    #se tiene que agregar todos los campos execpto los que se asignan en automatico 
    fields = ('Nombre', 'Descripcion','AñoLanzamiento','Duracion', 'Precio')
    login_url = 'login'
    permission_required = 'pages.admin_generic'

    def dispatch(self, request, *args, **kwargs):
      # if request.user.is_superuser:
           return super().dispatch(request, *args, **kwargs)
      # return HttpResponse('<h1> Que intentas hacer aqui? </h1>')


    def form_valid(self, form):
        form.instance.Creador = self.request.user
        return super().form_valid(form)
        ##obligas a la persona que este logeada
    


class PeliculaPageUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'pelicula_editar.html'
    model = Pelicula
    fields = ('Nombre', 'Descripcion', 'Precio')
    login_url = 'login'

    success_url = reverse_lazy('pelicula')

    permission_required = 'pages.admin_generic'



    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Creador != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PeliculaPageDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'pelicula_eliminar.html'
    model = Pelicula
    success_url = reverse_lazy('lista_pelicula')
    login_url = 'login'


class ResultadoBusquedaListView(ListView):
    template_name = 'resul_busqueda.html'
    model = Pelicula
    context_object_name = 'Todas_PeliculasBusquedas'
    #queryset = Pelicula.objects.filter(Nombre__icontains = 'Noche')




    def get_queryset(self):
        query = self.request.GET.get('q')
        return Pelicula.objects.filter(
            Q(Nombre__icontains=query)|Q(Nombre__icontains=query)
        )



 