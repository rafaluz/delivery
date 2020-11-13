from django.urls import path
from . import views  

urlpatterns = [
    path('olamundo', views.helloWorld),  
    # path('listar_produto_antigo', views.listarProdutos, name='listar_produto'),
    path('', views.ProdutoList.as_view(), name='listar_produto'),
    path('detalhar_produto/<int:pk>', views.produtoDetail.as_view(), name='detalhar_produto'),
    path('criar_produto', views.ProdutoCreate.as_view(), name="criar_produtos"),
    path('alterar_produto/<int:pk>', views.ProdutoUpdate.as_view(), name='alterar_produto'),
    path('deletar_produto/<int:pk>', views.ProdutoDelete.as_view(), name='deletar_produto'),
    # path('detalhar_produto/<int:id>', views.detalhesProduto, name='detalhar_produto'), 
]