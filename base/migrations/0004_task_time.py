# Generated by Django 4.0.3 on 2022-03-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_task_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
