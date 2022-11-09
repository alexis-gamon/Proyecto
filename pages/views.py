from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pelicula
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin##obliga a que estes logeado para poder visualizar una vista
from django.core.exceptions import PermissionDenied##valida los permisos
from django.http import HttpResponse
# Create your views here.


class PeliculaListView(ListView):
    model = Pelicula
    template_name = 'lista_pelicula.html'
    context_object_name = 'lista_pelicula'

 

# Create your views here.
class PeliculaTemplateView(LoginRequiredMixin, ListView):
    template_name = 'pelicula.html'
    model = Pelicula
    context_object_name = 'Todas_peliculas'

class homeTemplateView(TemplateView):
    template_name = 'home.html'



class PeliculaPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'pelicula_detalle.html'
    model = Pelicula
    context_object_name = 'Pelicula'

class PeliculaPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'pelicula_detalle.html'
    model = Pelicula
    context_object_name = 'Pelicula'
    login_url = 'login'
   

class PeliculaPagesCreate(LoginRequiredMixin,CreateView):
    template_name = 'pelicula_nueva.html'
    model = Pelicula
    #se tiene que agregar todos los campos execpto los que se asignan en automatico 
    fields = ('Nombre', 'Descripcion','AñoLanzamiento','Duracion')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
       if request.user.is_superuser:
           return super().dispatch(request, *args, **kwargs)
       return HttpResponse('<h1> Sin acceso </h1>')


    def form_valid(self, form):
        form.instance.Creador = self.request.user
        return super().form_valid(form)
        ##obligas a la persona que este logeada
    login_url = 'login'  


class PeliculaPageUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'pelicula_editar.html'
    model = Pelicula
    fields = ('Nombre', 'Descripcion')

    success_url = reverse_lazy('lista_pelicula')

    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Creador != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PeliculaPageDelete(LoginRequiredMixin, DeleteView):
    template_name = 'pelicula_eliminar.html'
    model = Pelicula
    success_url = reverse_lazy('lista_pelicula')

    login_url = 'login'
 



 