from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Articles(title=title, content=content)
    article.save()
    return redirect('articles:index')
    