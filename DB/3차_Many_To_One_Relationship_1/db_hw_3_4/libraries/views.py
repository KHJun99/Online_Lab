from django.shortcuts import render, redirect
from .models import Author
from .forms import BookForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    
    book_form = BookForm()
    
    context = {
        'author': author,
        'book_form' : book_form
    }
    return render(request, 'libraries/detail.html', context)

def book_create(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
        
    return redirect('libraries:detail', author_pk)
    