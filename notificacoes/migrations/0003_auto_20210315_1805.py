# Generated by Django 2.2.9 on 2021-03-15 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notificacoes', '0002_auto_20210315_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificacao',
            old_name='pedido_solicitado_id',
            new_name='pedido_solicitado',
        ),
        migrations.RenameField(
            model_name='notificacao',
            old_name='usuario_envia_id',
            new_name='usuario_envia',
        ),
        migrations.RenameField(
            model_name='notificacao',
            old_name='usuario_recebe_id',
            new_name='usuario_recebe',
        ),
    ]