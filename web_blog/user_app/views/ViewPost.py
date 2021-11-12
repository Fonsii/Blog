from django.http.response import HttpResponse
from django.views import generic
from django.shortcuts import HttpResponse
from user_app.models import Post
from user_app.models import Comments
from user_app.forms import AddCommentForm
from django.shortcuts import render
from django.contrib.auth.models import User


class ViewPost(generic.View):
    template_name = 'user_app/viewPost.html'
    form_class: AddCommentForm = AddCommentForm

    def get(self, request, post=None):
        if post is None:
            return HttpResponse("Post Not Found in URL")
        elif Post.objects.filter(id=post).exists():

            form = self.form_class()
            post = Post.objects.get(id=post)
            comments = Comments.objects.filter(post=post)
            context = {
                'form': form,
                'post': post,
                'comments': comments
            }
            return render(request, self.template_name, context)
        else:
            return HttpResponse("Post Not Found in Database")

    def post(self, request, email=None, post=None):
        form = self.form_class(request.POST)
        if form.is_valid():
            print('::VALID')
            print('::EMAIL', email)
            print('::EMAIL', request.POST.get('email'))
            if User.objects.filter(email=request.POST.get('email')).exists():
                print('::SAVE')
                comment = Comments(
                    post=Post.objects.get(id=post),
                    author=User.objects.get(email=request.POST.get('email')),
                    text=form.cleaned_data['text']
                )
                comment.save()
        return self.get(request, post)
