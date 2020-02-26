from django.shortcuts import render
from django.views.generic import (TemplateView,ListView)

class AboutView(TemplateView):
    template_name='about.html'

class PostListView(ListView):
    model=Post
