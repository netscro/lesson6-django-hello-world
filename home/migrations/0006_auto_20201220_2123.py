# Generated by Django 3.1.4 on 2020-12-20 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201215_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='normalized_name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
