# Generated by Django 3.0.5 on 2020-05-20 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hh', '0006_auto_20200521_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='picture',
            new_name='logo',
        ),
    ]