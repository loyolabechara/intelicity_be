# Generated by Django 3.0.2 on 2020-02-12 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacao', '0006_auto_20200212_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitacao',
            old_name='assunto_solicitacao',
            new_name='assuntosolicitacao',
        ),
    ]
