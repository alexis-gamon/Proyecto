
import stripe
from django.views.generic import TemplateView, DetailView
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import Permission
from pages.models import Pelicula
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin##obliga a que estes logeado para poder visualizar una vista


class OrderPelicula(LoginRequiredMixin, DetailView):
    template_name = 'orders/pago_pelicula.html'
    model = Pelicula
    context_object_name = 'Pelicula'
    login_url = 'login'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        context['api_key'] = settings.STRIPE_TEST_SECRET_KEY
        return context
    

def charge(request):


    if request.method == 'POST':
        precio = int(request.POST['Precio'])*100
        Nombre = request.POST['Nombre']
        charge = stripe.Charge.create(
            amount = precio, 
            currency = 'usd', 
            description = 'El pago de la pelicula: '+Nombre+' es de '+str(precio), 
            source = request.POST['stripeToken'],
            api_key = settings.STRIPE_TEST_SECRET_KEY
                                              )
        return render(request, 'orders/charge.html')

class OrdersPageView(TemplateView):
    model = Pelicula
    context_object_name = 'Todas_Peliculas'

    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        context['api_key'] = settings.STRIPE_TEST_SECRET_KEY
        return context


def charge2(request):
    permission = Permission.objects.get(codename='suscriptor')
    u = request.user
    u.user_permissions.add(permission)
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 10000, 
            currency = 'usd', 
            description = 'Pago Suscripcion', 
            source = request.POST['stripeToken'],
            api_key = settings.STRIPE_TEST_SECRET_KEY
                                              )
        return render(request, 'orders/charge.html')