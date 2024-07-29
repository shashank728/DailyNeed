# Generated by Django 5.0.6 on 2024-07-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_todo_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date',
        ),
        migrations.AddField(
            model_name='todo',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]