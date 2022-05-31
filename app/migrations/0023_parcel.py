# Generated by Django 4.0.4 on 2022-05-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_restorant'),
    ]

    operations = [
        migrations.CreateModel(
            name='parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seoul', models.IntegerField()),
                ('gangwon', models.IntegerField()),
                ('busan', models.IntegerField()),
                ('jeonbuk', models.IntegerField()),
                ('junnam', models.IntegerField()),
                ('jeju', models.IntegerField()),
            ],
            options={
                'db_table': 'parcel',
            },
        ),
    ]