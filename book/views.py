from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from .forms import BookForm


class List(generic.ListView):
    model = Book
    paginate_by = 3


class Detail(generic.DetailView):
    model = Book

class Create(generic.CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book:list')

    def form_valid(self,form):
        post_data = form.save(commit=False)
        post_data.user = self.request.user
        post_data.save()

        return super().form_valid(form)
    
class Update(generic.UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book:list')


class Delete(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('book:list')

# Create your views here.
