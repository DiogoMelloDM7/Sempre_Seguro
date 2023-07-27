# Generated by Django 4.2.3 on 2023-07-26 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0012_alter_usuario_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContasInformada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_vencimento', models.DateTimeField(default=django.utils.timezone.now)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contasinformadas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
