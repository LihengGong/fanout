# Generated by Django 2.1 on 2018-08-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20180827_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pushpinstatconn',
            name='conn_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='pushpinstatconn',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]