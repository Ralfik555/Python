# Generated by Django 3.1.4 on 2021-02-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210211_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
