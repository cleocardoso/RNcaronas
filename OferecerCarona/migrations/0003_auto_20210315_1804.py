# Generated by Django 2.2.9 on 2021-03-15 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OferecerCarona', '0002_oferecercarona_valortotal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oferecercarona',
            old_name='Usuario',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='oferecercarona',
            old_name='ValorTotal',
            new_name='valorTotal',
        ),
    ]
