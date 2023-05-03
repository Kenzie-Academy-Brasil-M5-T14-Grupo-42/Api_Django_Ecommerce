# Generated by Django 4.2.1 on 2023-05-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pedido Realizado', 'Pr'), ('Pedido Em Andamento', 'Pea'), ('Entregue', 'E')], default='Pedido Realizado')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('seller_id', models.IntegerField(default=None, null=True)),
                ('products', models.JSONField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]