# Generated by Django 4.0.4 on 2022-05-12 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_alter_respostas_id_dimensao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respostas',
            name='id_pessoa',
        ),
    ]
