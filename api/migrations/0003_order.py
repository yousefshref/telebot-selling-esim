# Generated by Django 5.1.4 on 2024-12-23 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_esim_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('esim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.esim')),
            ],
        ),
    ]
