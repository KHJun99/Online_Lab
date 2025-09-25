from django.shortcuts import render

# Create your views here.
def index(request):
    message = request.GET.get('message', '')
    context = {
        'message' : message,
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    
    return render(request, 'todos/create_todo.html')