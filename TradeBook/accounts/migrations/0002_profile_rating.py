# Generated by Django 3.0.8 on 2020-07-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
