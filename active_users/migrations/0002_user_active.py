# Generated by Django 2.0.5 on 2018-05-07 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
