# Generated by Django 3.1.4 on 2021-01-13 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210105_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ccy', models.CharField(max_length=100)),
                ('base_ccy', models.CharField(max_length=100)),
                ('buy', models.IntegerField(null=True)),
                ('sale', models.IntegerField(null=True)),
            ],
        ),
    ]
