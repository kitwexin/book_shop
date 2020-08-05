from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PublishingListView(ListView):
    model = models.Publishing
    template_name = 'publishing/list.html'
    paginate_by = 10

class PublishingCreateView(LoginRequiredMixin, CreateView):
    model = models.Publishing
    template_name = 'publishing/create.html'
    fields = ('name','description')
    def get_success_url(self):
        return reverse_lazy('publishing:list')

class PublishingUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Publishing
    template_name = 'publishing/update.html'
    fields = ('name','description')
    def get_success_url(self):
        return reverse_lazy('publishing:detail', kwargs = {'pk' : self.object.pk})

class PublishingDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Publishing
    template_name = 'publishing/delete.html'
    def get_success_url(self):
        return reverse_lazy('publishing:list')

class PublishingDetailView(DetailView):
    model = models.Publishing
    template_name = 'publishing/detail.html'
