# Generated by Django 5.0.6 on 2024-07-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_todo_date_todo_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('name', models.TextField()),
                ('number', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]