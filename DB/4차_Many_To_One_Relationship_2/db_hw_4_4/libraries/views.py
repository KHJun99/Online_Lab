from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = book.reviews.all()
    form = ReviewForm()

    context = {
        'book': book,
        'reviews' : reviews,
        'form' : form,
    }
    return render(request, 'libraries/detail.html', context)

@login_required
@require_POST
def review_create(request, book_pk):
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.book_id = book_pk
        review.user = request.user
        review.save()
    return redirect('libraries:detail', book_pk)


@login_required
@require_POST
def review_delete(request, book_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.user == review.user:
        review.delete()
    return redirect('libraries:detail', book_pk)