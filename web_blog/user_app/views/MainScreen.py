from django.views import generic
from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings

from user_app.models import Post
from django.contrib.auth.models import User
from admin_app.models import Category

def get_paginator_results(results, page_number):
    if results is not None:
        if page_number is None:
            page_number = 1

        paginator = Paginator(results, settings.PAGE_SIZE)
        page_display = paginator.get_page(page_number)
        return page_display
    return results

def get_results_filter_author(email):
    return Post.objects.filter(author__email=email).order_by("-created_date")

def get_results_filter_category(category):
    print(category)
    return Post.objects.filter(category__id=category).order_by("-created_date")

def get_all_results():
    return Post.objects.all().order_by("-created_date")

def get_all_authors():
    authors_id_list = Post.objects.order_by('-created_date').values_list('author__id').distinct()
    authors = User.objects.filter(id__in=authors_id_list)
    return authors

def get_all_categories():
    return Category.objects.all()
   
def do_filter(filter_post):
    posts = None

    filter_selector = list(filter_post.keys())[0]

    if filter_selector == "author":
        posts = get_results_filter_author(filter_post[filter_selector])
    elif filter_selector == "category":
        posts = get_results_filter_category(filter_post[filter_selector])
    
    return posts
    
def create_context(page_number, filter_post):
    posts = None

    if filter_post:
        posts = do_filter(filter_post)
    else:
        posts = get_all_results()

    page_display = get_paginator_results(posts, page_number)
    
    authors = get_all_authors()
    categories = get_all_categories()
    context ={
        'posts': page_display,
        'authors' : authors,
        'categories' : categories,
    }
    
    return context

class MainScreen(generic.View):

    def get(self, request):
        filter_post = {}
        if request.GET.get('author_email'):
            filter_post.update({'author': request.GET.get('author_email')})
        elif request.GET.get('categoria'):
            filter_post.update({'category': request.GET.get('categoria')})

        page_number = request.GET.get('pagina')
        return render(request, "user_app/index.html", create_context(page_number, filter_post))