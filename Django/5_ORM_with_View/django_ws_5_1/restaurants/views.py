from django.shortcuts import render, redirect
from .models import Restaurants

# Create your views here.
def index(request):
    restaurants = Restaurants.objects.all()
    context = {
        'restaurants' : restaurants
    }
    return render(request, 'restaurants/index.html', context)

def new(request):
    return render(request, 'restaurants/new.html')

def create(request):
    if request.method == 'POST':
        Restaurants.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('content'),
            address=request.POST.get('address'),
            phone_number=request.POST.get('number'),
        )
        return redirect('restaurants:index')
    
    return redirect('restaurants:new')