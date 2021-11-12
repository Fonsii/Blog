from django.views import generic
from django.shortcuts import redirect, render

from user_app.models import Post

class CreatePost(generic.View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'user_app/createPost.html')
        return redirect('index')

    def post(self, request):
        if request.user.is_authenticated:

            title = request.POST['titlePost']
            content = request.POST['contentPost']

            post_constructor = Post()
            post_constructor.author = request.user
            post_constructor.title = title
            post_constructor.text = content
            if 'imagePost' in request.FILES and request.FILES['imagePost'].name.endswith('.png'):
                file = request.FILES['imagePost']
                post_constructor.image = file

            post_constructor.save()

            return redirect('index')