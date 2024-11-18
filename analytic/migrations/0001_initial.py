# Generated by Django 5.1.2 on 2024-11-16 23:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('READ', 'READ'), ('ARCHIVED', 'ARCHIVED')], default='NEW', max_length=10)),
                ('notification_type', models.CharField(choices=[('VISIT_CREATED', 'VISIT_CREATED'), ('VISIT_CANCELLED', 'VISIT_CANCELLED'), ('OTHER', 'OTHER'), ('DOCTOR_DELETE', 'DOCTOR_DELETE'), ('PATIENT_DELETE', 'PATIENT_DELETE')], default='OTHER', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_notifications', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]