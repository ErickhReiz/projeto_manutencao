# Generated by Django 4.2.5 on 2023-09-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manutencoes',
            fields=[
                ('id_manucencao', models.AutoField(primary_key=True, serialize=False)),
                ('empresa', models.TextField(max_length=255)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]