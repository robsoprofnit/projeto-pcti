# Generated by Django 4.0.4 on 2022-05-12 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_remove_respostas_id_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='respostas',
            name='id_subindicador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastros.sub_indicadores', verbose_name='Sub-Indicador'),
            preserve_default=False,
        ),
    ]
