# Generated by Django 5.1.3 on 2024-11-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_reservation', '0007_alter_busschedule_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]