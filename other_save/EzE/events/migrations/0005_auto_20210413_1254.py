# Generated by Django 3.1.4 on 2021-04-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210413_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='skills',
            field=models.ManyToManyField(blank=True, to='events.Skills'),
        ),
    ]
