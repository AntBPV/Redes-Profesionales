# Generated by Django 5.1.1 on 2024-10-15 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_postmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='slug',
        ),
    ]
