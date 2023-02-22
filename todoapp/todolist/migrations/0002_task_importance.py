# Generated by Django 4.1.7 on 2023-02-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='importance',
            field=models.CharField(choices=[('imp', 'Important'), ('nim', 'Not important')], default='nim', max_length=3),
        ),
    ]
