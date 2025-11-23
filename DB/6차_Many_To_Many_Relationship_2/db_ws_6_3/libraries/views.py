from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Author, Book
from .forms import AuthorForm, BookForm

User = get_user_model()

# 메인 페이지
def index(request):
    return render(request, 'libraries/index.html')

# 유저 프로필 페이지
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    context = {
        'profile_user': profile_user,
    }
    return render(request, 'libraries/profile.html', context)

# 전체 책 조회 페이지
def books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'libraries/books.html', context)

# 작가 생성 기능
@login_required
def create_author(request):
    # 이미 작가인 경우에도 페이지 표시 (작가는 한 번만 생성 가능)
    if request.method == 'POST':
        # 이미 작가인지 확인
        if hasattr(request.user, 'author'):
            return redirect('libraries:profile', username=request.user.username)
        
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('libraries:profile', username=request.user.username)
    else:
        form = AuthorForm()
    
    context = {
        'form': form,
    }
    return render(request, 'libraries/create_author.html', context)

# 책 생성 기능
@login_required
def create_book(request):
    # 작가인지 확인
    if not hasattr(request.user, 'author'):
        return redirect('libraries:create_author')
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user.author
            book.save()
            return redirect('libraries:books')
    else:
        form = BookForm()
    
    context = {
        'form': form,
        'author': request.user.author,
    }
    return render(request, 'libraries/create_book.html', context)