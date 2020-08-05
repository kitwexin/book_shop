from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class AuthorListView(ListView):
    model = models.Author
    template_name = 'authors/list.html'
    paginate_by = 10

class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = models.Author
    template_name = 'authors/create.html'
    fields = ('name','description')
    def get_success_url(self):
        return reverse_lazy('authors:list')

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Author
    template_name = 'authors/update.html'
    fields = ('name','description')
    def get_success_url(self):
        return reverse_lazy('authors:detail', kwargs = {'pk' : self.object.pk})

class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Author
    template_name = 'authors/delete.html'
    def get_success_url(self):
        return reverse_lazy('authors:list')

class AuthorDetailView(DetailView):
    model = models.Author
    template_name = 'authors/detail.html'
