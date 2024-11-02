# Generated by Django 5.1.1 on 2024-11-02 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0005_profile_banner_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professionaldata',
            old_name='enterprise',
            new_name='company',
        ),
        migrations.RemoveField(
            model_name='educationaldata',
            name='school',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='educational_data',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='personal_data',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='professional_data',
        ),
        migrations.AddField(
            model_name='educationaldata',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='certificates/'),
        ),
        migrations.AddField(
            model_name='educationaldata',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='educational_data', to='UserProfile.profile'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='personal_data', to='UserProfile.profile'),
        ),
        migrations.AddField(
            model_name='professionaldata',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='professional_data', to='UserProfile.profile'),
        ),
    ]