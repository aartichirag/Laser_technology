from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from.models import category_master

# Create your views here.
class NewCategory(CreateView):
    model = category_master
    fields ='__all__'

class ViewCategory(ListView):
    model = category_master
    context_object_name = 'categorys'

class UpdateCategory(UpdateView):
    model = category_master
    fields = '__all__'

class DetailCategory(DetailView):
    model = category_master

class DeleteCategory(DeleteView):
    model =category_master
    success_url = '/category/view'