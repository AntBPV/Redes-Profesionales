# Generated by Django 5.1.1 on 2024-10-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_postmodel_public_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='title',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts_image/'),
        ),
    ]
