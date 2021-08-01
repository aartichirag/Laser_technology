from django.shortcuts import render
from models import product_info
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView

# Create your views here.
class NewProduct(CreateView):
    model = product_info
    fields = '__all__'

class ViewProduct(ListView):
    model = product_info
    context_object_name = 'products'

class UpdateProduct(UpdateView):
    model = product_info
    fields = '__all__'

class DetailProduct(DetailView):
    model = product_info

class DeleteProduct(DeleteView):
    model = product_info
    success_url = '/product/view'
