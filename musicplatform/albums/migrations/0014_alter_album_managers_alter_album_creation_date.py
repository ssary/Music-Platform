# Generated by Django 4.1.2 on 2022-10-15 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0013_alter_album_managers_alter_album_creation_date'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='album',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 9, 52, 50, 934344, tzinfo=datetime.timezone.utc)),
        ),
    ]