# Generated by Django 4.1.2 on 2022-10-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_alter_album_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creation_date',
            field=models.DateTimeField(verbose_name='2022-10-15T08:44:32.683832+00:00'),
        ),
    ]