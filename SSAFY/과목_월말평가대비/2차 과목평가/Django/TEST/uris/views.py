from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'uris/index.html')
    
def cube(request, num):
    ans = num **3
    return render(request, 'uris/cube.html', {'num':num, 'ans':ans})
    
def name(request):
    return render(request, 'uris/name.html')
    
def hello(request):
    name = request.POST.get('name')
    return render(request, 'uris/hello.html', {'name':name})