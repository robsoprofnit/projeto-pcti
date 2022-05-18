# Generated by Django 4.0.4 on 2022-05-18 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0011_indicadores_id_variavel'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoIndicadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, verbose_name='Nome Grupo Indicadorer')),
                ('descricao', models.TextField(verbose_name='Descrição do Grupo indicadores')),
                ('desativar', models.BooleanField()),
                ('id_dimensao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.dimensoes', verbose_name='Dimensão')),
            ],
            options={
                'verbose_name_plural': 'Gupos Indicadores',
            },
        ),
        migrations.DeleteModel(
            name='GrupoSubIndicadores',
        ),
    ]
