# Generated by Django 3.0.2 on 2020-02-05 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_agenda_assunto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agenda',
            options={'ordering': ['dt_evento', 'titulo']},
        ),
        migrations.AddField(
            model_name='agenda',
            name='titulo',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agenda',
            name='descricao',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
