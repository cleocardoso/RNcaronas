# Generated by Django 2.2.9 on 2021-03-14 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OferecerCarona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferecercarona',
            name='ValorTotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='valor'),
        ),
    ]
