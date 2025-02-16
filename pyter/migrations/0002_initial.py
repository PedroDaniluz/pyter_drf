# Generated by Django 5.1.6 on 2025-02-15 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pyter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=30)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instituicoes',
            fields=[
                ('id_instituicao', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Materiais',
            fields=[
                ('id_material', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('preco_kg', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('preco_m', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Situacoes',
            fields=[
                ('id_situacao', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('data_pedido', models.DateField()),
                ('data_prazo', models.DateField()),
                ('observacao', models.CharField(blank=True, max_length=100, null=True)),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='pyter.clientes')),
                ('id_instituicao', models.ForeignKey(db_column='id_instituicao', on_delete=django.db.models.deletion.DO_NOTHING, to='pyter.instituicoes')),
                ('id_situacao', models.ForeignKey(db_column='id_situacao', on_delete=django.db.models.deletion.DO_NOTHING, to='pyter.situacoes')),
            ],
        ),
        migrations.CreateModel(
            name='VariacoesProdutos',
            fields=[
                ('id_variacao', models.AutoField(primary_key=True, serialize=False)),
                ('tamanho', models.CharField(max_length=20)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('id_categoria', models.ForeignKey(db_column='id_categoria', on_delete=django.db.models.deletion.DO_NOTHING, to='pyter.categorias')),
                ('id_material', models.ForeignKey(db_column='id_material', on_delete=django.db.models.deletion.DO_NOTHING, to='pyter.materiais')),
                ('id_produto', models.ForeignKey(db_column='id_produto', on_delete=django.db.models.deletion.DO_NOTHING, to='pyter.produtos')),
            ],
        ),
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('id_pedido', models.ForeignKey(db_column='id_pedido', on_delete=django.db.models.deletion.DO_NOTHING, to='pyter.pedidos')),
                ('id_variacao', models.ForeignKey(db_column='id_variacao', on_delete=django.db.models.deletion.DO_NOTHING, to='pyter.variacoesprodutos')),
            ],
        ),
    ]
