# Generated by Django 4.2.1 on 2023-05-31 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_emails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='emails',
        ),
    ]