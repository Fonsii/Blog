from django.views import generic
from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings

from user_app.models import Post

def get_paginator_results(results, page_number):
        
    if page_number is None:
        page_number = 1

    paginator = Paginator(results, settings.PAGE_SIZE)
    page_display = paginator.get_page(page_number)
    return page_display

def create_context(page_number):
    posts = Post.objects.all().order_by("-created_date")
    page_display = get_paginator_results(posts, page_number)

    context ={
        'posts': page_display,
    }
    
    return context

class MainScreen(generic.View):

    def get(self, request):
        page_number = request.GET.get('pagina')
        return render(request, "user_app/index.html", create_context(page_number))