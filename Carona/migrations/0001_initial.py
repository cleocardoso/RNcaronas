# Generated by Django 2.2.9 on 2021-03-10 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OferecerCarona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(blank=True, max_length=255, null=True)),
                ('partida', models.CharField(blank=True, max_length=255, null=True)),
                ('oferecerCarona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OferecerCarona.oferecerCarona')),
            ],
            options={
                'db_table': 'Carona',
            },
        ),
    ]