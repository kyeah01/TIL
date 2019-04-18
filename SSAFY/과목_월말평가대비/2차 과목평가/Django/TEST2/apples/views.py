from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'apples/index.html')

def redirection(request):
    return redirect('/apple/')
    
def form_a(request):
    return render(request, 'apples/form_a.html')

def ans(request):
    name = request.POST.get('name')
    return render(request, 'apples/ans.html', {'name':name})