# Generated by Django 4.2.1 on 2023-05-31 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_emaillist_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaillist',
            name='attachment',
            field=models.FileField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='emaillist',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
