# Generated by Django 5.1.1 on 2024-10-16 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_postmodel_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='public',
            new_name='active',
        ),
    ]
