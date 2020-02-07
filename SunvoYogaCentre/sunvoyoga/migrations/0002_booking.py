# Generated by Django 3.0 on 2020-02-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunvoyoga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('mobnumber', models.CharField(max_length=60)),
                ('gender', models.CharField(max_length=100)),
                ('classes', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
