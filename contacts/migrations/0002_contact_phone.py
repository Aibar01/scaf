# Generated by Django 2.2.3 on 2019-07-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
