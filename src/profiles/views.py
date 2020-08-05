from django.views.generic import UpdateView, DetailView, TemplateView, CreateView, FormView
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

User = get_user_model()

class ProfileUpdate(UpdateView):
    model = models.Profile
    fields = ('__all__')
    template_name = 'profiles/update.html'
    
    def get_object(self):
        user_pk = self.kwargs.get('user_pk')
        obj, created = self.model.objects.get_or_create(
            user = User.objects.get(pk=user_pk),
            defaults = {}
        )
        return obj

class MyCab(TemplateView):
    template_name='profiles/mycab.html'

class CreateUser(FormView):
    form_class = UserCreationForm
    template_name = 'profiles/create_user.html'

    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super(CreateUser, self).form_valid(form)

    def form_invalid(self, form):
        return super(CreateUser, self).form_invalid(form)