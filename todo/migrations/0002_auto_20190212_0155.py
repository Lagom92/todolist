# Generated by Django 2.1.7 on 2019-02-12 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='userf',
            new_name='user',
        ),
    ]
