from django.http.response import HttpResponseRedirect
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponseRedirect

from user_app.models import Post
from admin_app.models import Category

def create_context():
    context = {}
    context['categories'] = Category.objects.all()
    return context

class CreatePost(generic.View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'user_app/createPost.html', create_context())
        return redirect('index')

    def post(self, request):
        if request.user.is_authenticated:
            try:
                title = request.POST['titlePost']
                content = request.POST['contentPost']
                category = request.POST['categoryPost']

                post_constructor = Post()
                post_constructor.author = request.user
                post_constructor.title = title
                post_constructor.text = content
                post_constructor.category = Category.objects.get(id=category)

                if 'imagePost' in request.FILES and request.FILES['imagePost'].name.endswith('.png'):
                    file = request.FILES['imagePost']
                    post_constructor.image = file

                post_constructor.save()

                messages.add_message(request, messages.INFO, 'Se creo la publicación correctamente')
                return HttpResponseRedirect(self.request.path_info) 
            except Exception as e:
                print(e)
                messages.add_message(request, messages.ERROR, 'Hubo un error al crear la publicación, intentelo más tarde')
                return HttpResponseRedirect(self.request.path_info) 