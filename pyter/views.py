from .models import *
from .serializers import *
from rest_framework import viewsets, generics
from django.db.models import Sum, F, Value, DecimalField
from django.db.models.functions import Coalesce


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer


class SituacoesViewSet(viewsets.ModelViewSet):
    queryset = Situacoes.objects.all()
    serializer_class = SituacoesSerializer


class InstituicoesViewSet(viewsets.ModelViewSet):
    queryset = Instituicoes.objects.all()
    serializer_class = InstituicoesSerializer


class MateriaisViewSet(viewsets.ModelViewSet):
    queryset = Materiais.objects.all()
    serializer_class = MateriaisSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


class ItensPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItensPedido.objects.all()
    serializer_class = ItensPedidoSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer


class VariacoesProdutosViewSet(viewsets.ModelViewSet):
    queryset = VariacoesProdutos.objects.all()
    serializer_class = VariacoesProdutosSerializer


class ListaVariacoesViewSet(generics.ListAPIView):
    queryset = VariacoesProdutos.objects.select_related().all()
    serializer_class = ListaVariacoesSerializer


class ListaPedidosViewSet(generics.ListAPIView):
    serializer_class = ListaPedidosSerializer

    def get_queryset(self):
        queryset = Pedidos.objects.annotate(
            situacao=F('id_situacao__nome'),
            cliente=F('id_cliente__nome'),
            data=F('data_pedido'),
            prazo=F('data_prazo'),
            instituicao=F('id_instituicao__nome'),
            valor=Coalesce(
                Sum(
                    F('itenspedido__quantidade') * F('itenspedido__id_variacao__preco'),
                    output_field=DecimalField(max_digits=10, decimal_places=2)
                ),
                Value(0.0),
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        ).order_by('id_pedido')

        return queryset


class PedidoInfoViewSet(generics.ListAPIView):
    serializer_class = PedidoInfoSerializer

    def get_queryset(self):
        id_pedido = self.kwargs.get('id_pedido', None)
        queryset = Pedidos.objects.annotate(
            nome=F('id_cliente__nome'),
            telefone=F('id_cliente__telefone'),
            email=F('id_cliente__email'),
            data=F('data_pedido'),
            prazo=F('data_prazo'),
            instituicao=F('id_instituicao__nome'),
        )

        if id_pedido is not None:
            queryset = queryset.filter(id_pedido = id_pedido)

        return queryset


class PedidoItensViewSet(generics.ListAPIView):
    serializer_class = PedidoItensSerializer

    def get_queryset(self):
        id_pedido = self.kwargs.get('id_pedido', None)
        queryset = ItensPedido.objects.annotate(
            produto=F('id_variacao__id_produto__nome'),
            categoria=F('id_variacao__id_categoria__nome'),
            material=F('id_variacao__id_material__nome'),
            tamanho=F('id_variacao__tamanho'),
            observacoes=F('id_pedido__observacao'),
            valor=F('id_variacao__preco') * F('quantidade'),
        )

        if id_pedido is not None:
            queryset = queryset.filter(id_pedido = id_pedido)

        return queryset