# Generated by Django 3.0.5 on 2020-05-20 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hh', '0005_auto_20200520_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(blank=True, default=None, height_field='height_field', null=True, upload_to='speciality_images', width_field='width_field'),
        ),
    ]