# Generated by Django 3.0.5 on 2020-04-24 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20200424_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='notes',
            new_name='content',
        ),
    ]
