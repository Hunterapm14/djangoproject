# Generated by Django 3.2.9 on 2022-09-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
