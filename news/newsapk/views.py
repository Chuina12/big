from django.shortcuts import render
from  . models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

# Create your views here.

def index(request):
    product = Article.objects.all()
    return render(request, 'index.html',{'product':product})

def base(request):
    product = Article.objects.all()
    return render(request, 'index.html',{'product':product})


class produitDetailView(DetailView):
    model = Article
    template_name = 'read.html'
