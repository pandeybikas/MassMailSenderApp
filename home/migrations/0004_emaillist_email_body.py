# Generated by Django 4.2.1 on 2023-05-31 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_emaillist_attachment_emaillist_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaillist',
            name='email_body',
            field=models.TextField(null=True),
        ),
    ]
