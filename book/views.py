from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Book
from .forms import BookForm


class List(generic.ListView):
    model = Book
    paginate_by = 5
    ordering = '-posted_date'
           
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
    paginate_by = 5

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = Book.objects.filter(user=user_id).order_by('-posted_date')

        return user_list
    

class Mypage(generic.ListView):

    template_name = 'book/mypage.html'
    paginate_by = 5

    def get_queryset(self):
        querySet = Book.objects.filter(user=self.request.user).order_by('-posted_date')

        return querySet
    

class Category(generic.ListView):
    template_name = 'book/book_list.html'
    paginate_by = 5

    def get_queryset(self):
        category_id = self.kwargs['document_type']
        category_list = Book.objects.filter(document_type=category_id).order_by('-posted_date')

        return category_list
    
class PeopleList(generic.ListView):
    model = Book
    form_class = BookForm
    
    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            people_list = Book.objects.filter(
                book_title__icontains=query)
        else:
            people_list = Book.objects.all()
        return people_list