from django.views import generic
from django.shortcuts import render
from admin_app.models import Category
from admin_app.forms import AddCategoryForm

from django.shortcuts import redirect


class AdministrationView(generic.View):
    template_name = 'admin_app/administration_categories.html'
    form_class: AddCategoryForm = AddCategoryForm

    def get(self, request, category=None):

        form = self.form_class()
        selected_category = None

        if request.GET.get('accion') == 'editar':
            category_to_edit = Category.objects.get(pk=category)
            form = self.form_class(instance=category_to_edit)
            selected_category = category_to_edit
        elif request.GET.get('accion') == 'borrar':
            category_to_delete = Category.objects.get(pk=category)
            category_to_delete.delete()
            return redirect('administration_categories')

        context = {
            'form': form,
            'categories': Category.objects.all(),
            'selected_category': selected_category
        }
        return render(request, self.template_name, context)

    def post(self, request, category=None):
        form = self.form_class(request.POST)
        if form.is_valid():
            if category is not None:
                category_to_edit = Category.objects.get(pk=category)
                category_to_edit.name = form.cleaned_data['name']
                category_to_edit.description = form.cleaned_data['description']
                category_to_edit.save()
            else:
                form.save()
        return redirect('administration_categories')
