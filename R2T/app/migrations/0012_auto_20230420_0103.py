# Generated by Django 3.2.5 on 2023-04-19 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_name_room_roomid'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='customer',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='translator',
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
    ]
