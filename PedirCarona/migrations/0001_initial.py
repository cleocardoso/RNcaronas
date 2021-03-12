# Generated by Django 2.2.9 on 2021-03-10 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0003_auto_20210310_1638'),
        ('Carona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pedirCarona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataPedCarona', models.DateField(blank=True, null=True)),
                ('quantidadeVagas', models.IntegerField(verbose_name='quantidade de vagas')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Usuario', to='usuario.usuario')),
                ('carona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Carona', to='Carona.Carona')),
            ],
            options={
                'db_table': 'pedirCarona',
            },
        ),
    ]