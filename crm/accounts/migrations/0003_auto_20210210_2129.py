# Generated by Django 3.1.4 on 2021-02-10 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[(1, 'Indoor'), (2, 'Out Door')], max_length=200, null=True),
        ),
    ]