# Generated by Django 4.1.6 on 2023-02-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
