# Generated by Django 5.1.2 on 2024-11-14 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templatesApp', '0005_alter_usuario_options_alter_usuario_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['rut'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
