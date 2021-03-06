# Generated by Django 3.0 on 2020-02-02 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estagio', models.CharField(max_length=120)),
                ('descricao', models.CharField(max_length=2000)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Dirigente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Ponto_Apoio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('diretor', models.CharField(blank=True, max_length=60, null=True)),
                ('celular', models.CharField(max_length=11)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('endereco', models.CharField(max_length=120)),
                ('numero', models.CharField(max_length=120)),
                ('complemento', models.CharField(blank=True, max_length=120, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Bairro')),
                ('dirigente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dcivil.Dirigente')),
                ('responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dcivil.Responsavel')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Historico_Alerta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('alerta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dcivil.Alerta')),
            ],
            options={
                'ordering': ['-dt_inclusao'],
            },
        ),
    ]
