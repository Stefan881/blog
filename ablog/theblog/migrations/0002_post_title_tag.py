# Generated by Django 4.2.4 on 2023-08-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="My Freakin' Awesome Blog!", max_length=255),
        ),
    ]
