# Generated by Django 4.1.2 on 2022-10-15 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_alter_album_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 9, 18, 54, 844291)),
        ),
    ]
