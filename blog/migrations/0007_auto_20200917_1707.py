# Generated by Django 3.1.1 on 2020-09-17 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_eventos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Eventos',
            new_name='Evento',
        ),
    ]
