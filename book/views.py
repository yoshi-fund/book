from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from .forms import BookForm


class List(generic.ListView):
    model = Book
    paginate_by = 4

class Detail(generic.DetailView):
    model = Book
    def get_queryset(self):
        return Book.objects.all().order_by('-posted_date')

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


class UserView(generic.ListView):
    
    template_name = 'book/book_list.html'
    paginate_by = 3

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = Book.objects.filter(user=user_id).order_by('-posted_date')

        return user_list
    

class Mypage(generic.ListView):

    template_name = 'book/mypage.html'
    paginate_by = 1

    def get_queryset(self):
        querySet = Book.objects.filter(user=self.request.user).order_by('-posted_date')

        return querySet
