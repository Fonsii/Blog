from django.http.response import HttpResponse
from django.views import generic
from django.shortcuts import HttpResponse

class SeePost(generic.View):

    def get(self, request, post_title):
        return HttpResponse("SeePost")
