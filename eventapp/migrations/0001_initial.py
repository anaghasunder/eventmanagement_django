# Generated by Django 4.2.5 on 2023-09-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=120)),
                ('event_location', models.CharField(max_length=60)),
                ('date', models.CharField(max_length=120)),
            ],
        ),
    ]
