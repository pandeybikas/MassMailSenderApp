# Generated by Django 4.2.1 on 2023-05-31 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='emails',
            field=models.ManyToManyField(to='home.emaillist'),
        ),
    ]
