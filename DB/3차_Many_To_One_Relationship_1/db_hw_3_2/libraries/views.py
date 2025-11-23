from django.shortcuts import render, redirect
from .models import Author
from .forms import BookForm


# Create your views here.
def index(request):
    author_list = Author.objects.all()
    
    context = {
        'author_list': author_list
    }
    
    return render(request, 'libraries/index.html', context)


def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    
    book_form = BookForm()
    
    context = {
        'author': author,
        'book_form': book_form
    }
    return render(request, 'libraries/detail.html', context)