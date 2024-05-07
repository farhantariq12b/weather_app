# Generated by Django 2.2 on 2024-05-07 14:22

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('detailing_type', models.CharField(blank=True, max_length=20, null=True)),
                ('data', jsonfield.fields.JSONField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'unique_together': {('latitude', 'longitude', 'detailing_type')},
            },
        ),
    ]
