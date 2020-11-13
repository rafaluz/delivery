from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
from delivery.pedido.models import Produto
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

def helloWorld(request):
    return HttpResponse('Olá mundo!')
    

# def listarProdutos(request):
#     produtos = Produto.objects.all()

#     return render(request, 'produto/produto_list.html', {'produtos':produtos})


# def detalhesProduto(request,id):

#     produto = Produto.objects.get(id=id)

#     return render(request, 'produto/produto_details.html', {'produto':produto})


# classes baseadas em views

class ProdutoList(ListView):
    model = Produto
    template_name = 'produto/produto_list.html'


class produtoDetail(DetailView):
    model = Produto
    template_name = 'produto/produto_details.html'


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto/produto_create.html'
    fields = ['nome','valor']

    def get_success_url(self):
        return reverse('listar_produto')



class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto/produto_create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('listar_produto')


class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'produto/produto_confirm_delete.html'
    success_url = reverse_lazy('listar_produto')
