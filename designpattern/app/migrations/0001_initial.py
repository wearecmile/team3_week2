# Generated by Django 4.2.3 on 2023-07-14 04:40

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model_id', models.CharField(default=app.models.generate_car_model_id, max_length=5)),
                ('car_name', models.CharField(max_length=100)),
                ('car_details', models.TextField(blank=True, null=True)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.car')),
            ],
        ),
    ]
