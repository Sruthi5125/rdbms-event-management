# Generated by Django 5.1.1 on 2024-09-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_departments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departments',
            name='id',
        ),
        migrations.RemoveField(
            model_name='events',
            name='id',
        ),
        migrations.AlterField(
            model_name='departments',
            name='did',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='events',
            name='eid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('vid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('vname', models.CharField(max_length=100)),
                ('vblock', models.CharField(max_length=100)),
                ('vcapacity', models.CharField(max_length=100)),
                ('vevents', models.ManyToManyField(to='newapp.events')),
            ],
            options={
                'db_table': 'Venue',
            },
        ),
    ]