# Generated by Django 4.0.2 on 2022-02-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_follows_profile_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(to='user.Profile'),
        ),
    ]
