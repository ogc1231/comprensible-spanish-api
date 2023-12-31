# Generated by Django 3.2.21 on 2023-09-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0009_alter_resource_difficulty_level_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='difficulty_level_filter',
            field=models.CharField(choices=[('learner', 'Learner'), ('easy_native', 'Easy Native'), ('native', 'Native')], default='all', max_length=32),
        ),
    ]
