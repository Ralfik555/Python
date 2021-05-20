# Generated by Django 3.1.4 on 2021-04-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20210413_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Ongoing', 'Ongoing'), ('Finished', 'Finished')], max_length=200, null=True),
        ),
    ]