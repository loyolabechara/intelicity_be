# Generated by Django 3.0.2 on 2020-02-12 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0003_auto_20200212_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='situacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='solicitacao.Situacao'),
        ),
    ]
