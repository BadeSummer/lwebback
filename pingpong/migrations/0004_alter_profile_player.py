# Generated by Django 5.0.4 on 2024-04-26 02:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pingpong', '0003_profile_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='pingpong.player', verbose_name='选手'),
        ),
    ]
