# Generated by Django 4.2.2 on 2023-07-10 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0002_conta_usuario_recebimento_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='futuras_compras',
        ),
        migrations.AddField(
            model_name='futurascompra',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='futurascompras', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='conta',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contas_usuarios', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recebimento',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recebimentos_usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
