from .forms import CustomUserCreationForm

from django.urls import reverse_lazy

from django.views.generic import CreateView, TemplateView


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class homeTemplateView(TemplateView):
    template_name = 'home.html'

