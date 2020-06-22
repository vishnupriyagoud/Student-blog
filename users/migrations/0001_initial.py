# Generated by Django 3.0.7 on 2020-06-17 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('signup_date', models.DateTimeField(auto_now_add=True)),
                ('lastlogin_date', models.DateTimeField(auto_now=True)),
                ('reported_users', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
