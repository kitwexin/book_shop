from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class BooksListView(ListView):
    model = models.Book
    template_name = 'books/list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        key1 = self.request.GET.get('key1')
        print(key1)
        return super().get_context_data(**kwargs)


class BooksCreateView(LoginRequiredMixin, CreateView):
    model = models.Book
    template_name = 'books/create.html'
    fields = ('__all__')
    def get_success_url(self):
        return reverse_lazy('books:list')

class BooksUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Book
    template_name = 'books/update.html'
    fields = ('__all__')
    def get_success_url(self):
        return reverse_lazy('books:detail', kwargs = {'pk' : self.object.pk})

class BooksDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Book
    template_name = 'books/delete.html'
    def get_success_url(self):
        return reverse_lazy('books:list')

class BooksDetailView(DetailView):
    model = models.Book
    template_name = 'books/detail.html'

class HomePage(ListView):
    model = models.Book
    template_name = 'books/home_page.html'