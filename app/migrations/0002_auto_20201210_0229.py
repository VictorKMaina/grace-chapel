# Generated by Django 3.1.4 on 2020-12-09 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='friends_count',
            new_name='adults_count',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='date_visited',
        ),
    ]
