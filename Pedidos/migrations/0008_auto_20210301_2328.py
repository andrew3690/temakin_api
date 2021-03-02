# Generated by Django 3.1.5 on 2021-03-01 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0007_auto_20210301_1906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrega',
            options={'verbose_name_plural': 'Entregas'},
        ),
        migrations.AlterModelOptions(
            name='funcionarios',
            options={'verbose_name_plural': 'Funcionarios'},
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='user',
        ),
        migrations.AddField(
            model_name='entrega',
            name='descarga',
            field=models.CharField(choices=[('MEP', 'Maquinario Extremamente Pesado'), ('MP', 'Maqunario Pesado'), ('NN', 'Nao Necessita')], default='esperando', max_length=40),
        ),
    ]
