# Generated by Django 3.1.4 on 2021-04-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210413_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='approved',
            field=models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], default=('NO', 'NO'), max_length=200),
        ),
    ]