# Generated by Django 3.1.1 on 2020-09-16 23:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dataHoraEvento',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]