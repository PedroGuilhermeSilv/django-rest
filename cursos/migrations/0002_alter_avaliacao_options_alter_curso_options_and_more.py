# Generated by Django 5.0.2 on 2024-02-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'ordering': ['id'], 'verbose_name': 'Avaliação', 'verbose_name_plural': 'Avaliações'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['id'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='id',
            field=models.TextField(default='<function uuid4 at 0x7f07a86195a0>', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.TextField(default='<function uuid4 at 0x7f07a86195a0>', editable=False, primary_key=True, serialize=False),
        ),
    ]
