# Generated by Django 5.1.2 on 2024-11-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_schedule_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(),
        ),
    ]