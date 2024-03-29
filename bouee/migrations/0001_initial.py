# Generated by Django 4.2.7 on 2023-11-28 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bouee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('dateofcreation', models.CharField(max_length=25)),
                ('serienumber', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Donnees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=30)),
                ('lattitude', models.CharField(max_length=10)),
                ('longitude', models.CharField(max_length=10)),
                ('altitude', models.CharField(max_length=10)),
                ('nombredesattelite', models.CharField(max_length=2)),
                ('temp', models.CharField(max_length=6)),
                ('hum', models.CharField(max_length=6)),
                ('press', models.CharField(max_length=6)),
                ('bouee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouee.bouee')),
            ],
        ),
    ]
