# Generated by Django 3.1.4 on 2020-12-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201206_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='social_url',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
