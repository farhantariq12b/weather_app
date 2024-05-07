# Generated by Django 2.2 on 2024-05-07 09:46

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('data_type', models.CharField(max_length=20)),
                ('data', jsonfield.fields.JSONField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
