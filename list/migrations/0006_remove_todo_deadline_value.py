# Generated by Django 5.1.6 on 2025-02-24 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_todo_deadline_value_alter_todo_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='deadline_value',
        ),
    ]
