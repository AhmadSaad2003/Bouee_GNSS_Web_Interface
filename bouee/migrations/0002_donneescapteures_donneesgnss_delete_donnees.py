# Generated by Django 4.2.7 on 2024-01-30 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bouee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonneesCapteures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=30)),
                ('temp', models.CharField(max_length=6)),
                ('hum', models.CharField(max_length=6)),
                ('press', models.CharField(max_length=6)),
                ('bouee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouee.bouee')),
            ],
        ),
        migrations.CreateModel(
            name='DonneesGnss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=30)),
                ('lattitude', models.CharField(max_length=10)),
                ('longitude', models.CharField(max_length=10)),
                ('altitude', models.CharField(max_length=10)),
                ('nombredesattelite', models.CharField(max_length=2)),
                ('bouee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bouee.bouee')),
            ],
        ),
        migrations.DeleteModel(
            name='Donnees',
        ),
    ]