# Generated by Django 4.0.4 on 2022-05-23 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0019_remove_respostas_tag_remove_variavel_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respostas',
            name='desativar',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='respostas',
            name='id_pessoa_juridica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.pessoa_juridica', verbose_name='Instituição'),
        ),
        migrations.AlterField(
            model_name='respostas',
            name='resposta',
            field=models.FloatField(verbose_name='Resposta'),
        ),
        migrations.AlterUniqueTogether(
            name='respostas',
            unique_together={('id_relatorio', 'id_variavel')},
        ),
    ]
