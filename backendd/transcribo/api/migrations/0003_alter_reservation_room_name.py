# Generated by Django 4.2.5 on 2023-09-22 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_equipment_refreshment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room_name',
            field=models.CharField(choices=[('Board room1', 'Board room1'), ('Board room2', 'Board room2'), ('Board room3', 'Board room3'), ('Board room4', 'Board room4')], max_length=255),
        ),
    ]
