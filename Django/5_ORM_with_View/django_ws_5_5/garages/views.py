from django.shortcuts import render, redirect, get_object_or_404
from .models import Garage

def index(request):
    garages = Garage.objects.all()
    return render(request, 'garages/index.html', {'garages': garages})

def new(request):
    return render(request, 'garages/new.html')

def create(request):
    if request.method == 'POST':
        location = request.POST.get('location') or ''
        capacity = request.POST.get('capacity') or 0
        is_parking_available = request.POST.get('is_parking_available')
        opening_time = request.POST.get('opening_time') or None
        closing_time = request.POST.get('closing_time') or None

        Garage.objects.create(
            location=location,
            capacity=capacity,
            is_parking_available=is_parking_available,
            opening_time=opening_time,
            closing_time=closing_time,
        )
        return redirect('garages:index')
    return redirect('garages:new')

def edit(request, pk):
    garage = get_object_or_404(Garage, pk=pk)
    return render(request, 'garages/edit.html', {'garage': garage})

def update(request, pk):
    garage = get_object_or_404(Garage, pk=pk)
    if request.method == 'POST':
        garage.location = request.POST.get('location') or garage.location
        garage.capacity = request.POST.get('capacity') or garage.capacity
        garage.is_parking_available = request.POST.get('is_parking_available')
        garage.opening_time = request.POST.get('opening_time') or None
        garage.closing_time = request.POST.get('closing_time') or None
        garage.save()
        return redirect('garages:index')
    return redirect('garages:edit', pk=pk)

def delete(request, pk):
    garage = get_object_or_404(Garage, pk=pk)
    if request.method == 'POST':
        garage.delete()
    return redirect('garages:index')
