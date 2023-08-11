from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from fidbeck.models import Fidbeck


class Fidbeckcreateview(CreateView):
    model = Fidbeck
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('fidbeck:list')


    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)




class FidbecklistView(ListView):
    model = Fidbeck

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class Fidbecdetaileview(DetailView):
    model = Fidbeck

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object



class Fidbecupdateview(UpdateView):
    model = Fidbeck
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('fidbeck:list')

    # def get_success_url(self):
    #     return reverse('fidbeck:view', args=[self.kwargs.get('pk')])


class FidbecdeleteView(DeleteView):
    model = Fidbeck
    success_url = reverse_lazy('fidbeck:list')


