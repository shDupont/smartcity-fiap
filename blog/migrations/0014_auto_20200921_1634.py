# Generated by Django 3.1.1 on 2020-09-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200921_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bannerEvento',
            field=models.ImageField(upload_to='blog/static/img'),
        ),
    ]