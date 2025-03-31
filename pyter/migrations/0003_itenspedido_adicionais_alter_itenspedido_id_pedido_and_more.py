# Generated by Django 5.1.6 on 2025-03-30 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyter', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itenspedido',
            name='adicionais',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itenspedido',
            name='id_pedido',
            field=models.ForeignKey(db_column='id_pedido', on_delete=django.db.models.deletion.CASCADE, to='pyter.pedidos'),
        ),
        migrations.AlterField(
            model_name='variacoesprodutos',
            name='id_categoria',
            field=models.ForeignKey(db_column='id_categoria', on_delete=django.db.models.deletion.CASCADE, to='pyter.categorias'),
        ),
        migrations.AlterField(
            model_name='variacoesprodutos',
            name='id_material',
            field=models.ForeignKey(db_column='id_material', on_delete=django.db.models.deletion.CASCADE, to='pyter.materiais'),
        ),
        migrations.AlterField(
            model_name='variacoesprodutos',
            name='id_produto',
            field=models.ForeignKey(db_column='id_produto', on_delete=django.db.models.deletion.CASCADE, to='pyter.produtos'),
        ),
    ]
