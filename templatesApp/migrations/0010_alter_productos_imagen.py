# Generated by Django 5.1.2 on 2024-11-21 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatesApp', '0009_alter_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imgproduct/'),
        ),
    ]
