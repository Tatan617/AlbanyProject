# Generated by Django 5.1.2 on 2024-11-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]