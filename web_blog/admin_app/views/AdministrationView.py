from django.views import generic


class AdministrationView(generic.View):
    template_name = 'admin_app/administration.html'
    pass
