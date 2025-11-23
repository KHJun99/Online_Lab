from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Author, Book
from .forms import AuthorForm, BookForm

# Create your views here.
def index(request):
    return render(request, 'libraries/index.html')

@login_required
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('accounts:profile', author.user.username)
    else:
        form = AuthorForm()
    context = {
        'form': form
    }
    return render(request, 'libraries/create_author.html', context)

def books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/books.html', context)

@login_required
def books_create(request):
    if request.method == 'POST':
        form = BookForm(request.user, request.POST)  # user 정보 전달!
        if form.is_valid():
            form.save()
            return redirect('libraries:books')
    else:
        form = BookForm(request.user)  # user 정보 전달!
    context = {
        'form': form
    }
    return render(request, 'libraries/books_create.html', context)

def author_books(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    books = author.book_set.all()
    
    # 구독자 수 추가
    subscribers_count = author.subscribed_users.count()
    
    context = {
        'author': author,
        'books': books,
        'subscribers_count': subscribers_count,
    }
    return render(request, 'libraries/author_books.html', context)

@login_required
def author_subscribed(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    
    if request.method == 'POST':
        if author.subscribed_users.filter(pk=request.user.pk).exists():
            author.subscribed_users.remove(request.user)
        else:
            author.subscribed_users.add(request.user)
    
    return redirect('libraries:author_books', author.pk)