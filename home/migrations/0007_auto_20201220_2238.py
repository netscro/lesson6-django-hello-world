# Generated by Django 3.1.4 on 2020-12-20 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201220_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='normalized_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]