# Generated by Django 3.2.21 on 2023-09-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_alter_resource_difficulty_level_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='difficulty_level_filter',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('easy_native', 'Easy Native'), ('adv_native', 'Adv Native')], default='all', max_length=32),
        ),
    ]
