# Generated by Django 4.0.3 on 2022-04-27 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vegetable_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegetablename', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('img', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'vegetable',
            },
        ),
    ]
