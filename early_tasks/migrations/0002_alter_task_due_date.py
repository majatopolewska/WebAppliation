# Generated by Django 5.1.1 on 2024-10-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('early_tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
