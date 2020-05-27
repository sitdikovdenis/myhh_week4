# Generated by Django 3.0.5 on 2020-05-27 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hh', '0008_auto_20200525_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('not_looking', 'Не ищу работу'), ('considering', 'Рассматриваю предложения'), ('looking', 'Ищу работу')], default='looking', max_length=15)),
                ('salary', models.IntegerField()),
                ('grade', models.CharField(choices=[('trainee', 'Стажер'), ('junior', 'Джуниор'), ('middle', 'Миддл'), ('signor', 'Синьор'), ('lead', 'Лид')], default='looking', max_length=15)),
                ('education', models.CharField(max_length=1024)),
                ('experience', models.CharField(max_length=4096)),
                ('portfolio', models.CharField(max_length=8000)),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='hh.Specialty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
