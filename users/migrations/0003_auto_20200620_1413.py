# Generated by Django 3.0.7 on 2020-06-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('post_date', models.DateTimeField()),
                ('post_title', models.CharField(max_length=100)),
                ('post_content', models.CharField(max_length=400)),
                ('reported_user', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'blogs',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
