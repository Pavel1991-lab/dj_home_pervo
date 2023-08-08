from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from fidbeck.models import Fidbeck


class Fidbeckcreateview(CreateView):
    model = Fidbeck
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('fidbeck:list')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_mat = form.save()
    #         new_mat.slug = slugify(new_mat.title)
    #         new_mat.save()
    #     return super().form_valid(form)

class FidbecklistView(ListView):
    model = Fidbeck

class Fidbecdetaileview(DetailView):
    model = Fidbeck


class Fidbecupdateview(UpdateView):
    model = Fidbeck
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('fidbeck:list')

class FidbecdeleteView(DeleteView):
    model = Fidbeck
    success_url = reverse_lazy('fidbeck:list')


