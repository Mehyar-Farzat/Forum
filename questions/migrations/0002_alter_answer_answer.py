# Generated by Django 4.2 on 2023-08-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(max_length=10000),
        ),
    ]
