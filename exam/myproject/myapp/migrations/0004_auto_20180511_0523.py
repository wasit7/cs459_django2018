# Generated by Django 2.0 on 2018-05-11 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_room_isavailable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
