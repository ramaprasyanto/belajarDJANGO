from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'blog.html')

def resent(request):
  return render (request,'resent.html')