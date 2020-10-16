from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
from django.urls import reverse_lazy # new

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'index.html'

def portfolio(request):
    return render(request, 'portfolio.html')