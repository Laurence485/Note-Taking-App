# Generated by Django 3.0.5 on 2020-04-24 14:45

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20200422_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='notes',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
