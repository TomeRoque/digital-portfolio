# Generated by Django 4.0.4 on 2022-06-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='concluido',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='prioridade',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='titulo',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='comentario',
            field=models.CharField(default='anonimo', max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='nome',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
