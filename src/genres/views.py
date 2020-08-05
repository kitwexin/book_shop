from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class GenreListView(ListView):
    model = models.Genre
    template_name = 'genres/list.html'
    paginate_by = 10

class GenreCreateView(LoginRequiredMixin, CreateView):
    model = models.Genre
    template_name = 'genres/create.html'
    fields = ('name','description')
    def get_success_url(self):
        return reverse_lazy('genres:list')

class GenreUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Genre
    template_name = 'genres/update.html'
    fields = ('name','description')
    def get_success_url(self):
        return reverse_lazy('genres:detail', kwargs = {'pk' : self.object.pk})

class GenreDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Genre
    template_name = 'genres/delete.html'
    def get_success_url(self):
        return reverse_lazy('genres:list')

class GenreDetailView(DetailView):
    model = models.Genre
    template_name = 'genres/detail.html'
