from django.views import generic
from django.shortcuts import render

class AdministrationView(generic.View):
    template_name = 'admin_app/administration.html'
    
    def get(self, request):
        return render(request, self.template_name)
