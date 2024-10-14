# Generated by Django 5.1.1 on 2024-09-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=120)),
                ('text', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=120, unique=True)),
            ],
        ),
    ]