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
    # 작가인지 확인
    try:
        author = request.user.author
    except:
        return redirect('libraries:create_author')
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect('libraries:books')
    else:
        form = BookForm()
    
    context = {
        'form': form,
        'author': author,
    }
    return render(request, 'libraries/books_create.html', context)

# 작가 프로필 페이지
def author_detail(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    books = author.book_set.all()
    
    # 작가의 총 독립(구독자) 수
    subscribers_count = author.subscribed_users.count()
    
    context = {
        'author': author,
        'books': books,
        'subscribers_count': subscribers_count,
    }
    return render(request, 'libraries/author_detail.html', context)

# 작가 구독/구독 취소 기능
@login_required
def author_subscribe(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    
    if request.method == 'POST':
        # 이미 구독 중이면 구독 취소, 아니면 구독
        if request.user in author.subscribed_users.all():
            author.subscribed_users.remove(request.user)
        else:
            author.subscribed_users.add(request.user)
    
    return redirect('libraries:author_detail', author_pk=author.pk)