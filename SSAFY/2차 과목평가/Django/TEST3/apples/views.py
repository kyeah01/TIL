from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'apples/index.html')

def read(request):

def delete(request):
    pk = request.GET.get('')
    board = Board.objects.get(pk=pk)