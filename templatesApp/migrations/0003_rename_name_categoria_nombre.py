# Generated by Django 5.1.2 on 2024-11-14 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templatesApp', '0002_productos_habilitado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='name',
            new_name='nombre',
        ),
    ]