# Generated by Django 4.1.2 on 2022-10-14 22:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Album', max_length=100)),
                ('creation_date', models.DateTimeField(verbose_name=datetime.datetime(2022, 10, 14, 22, 43, 2, 653910, tzinfo=datetime.timezone.utc))),
                ('released_date', models.DateTimeField()),
                ('cost', models.DecimalField(decimal_places=4, max_digits=10)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.artist')),
            ],
        ),
    ]