# Generated by Django 3.0.7 on 2020-06-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200620_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('lastlogin', models.DateTimeField()),
                ('password', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'admins',
                'managed': False,
            },
        ),
    ]