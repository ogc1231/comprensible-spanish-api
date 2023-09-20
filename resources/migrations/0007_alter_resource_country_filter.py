# Generated by Django 3.2.21 on 2023-09-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_rename_description_resource_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='country_filter',
            field=models.CharField(choices=[('mixed', 'Mixed'), ('argentina', 'Argentina'), ('bolivia', 'Bolivia'), ('canary_islands', 'Canary Islands'), ('chile', 'Chile'), ('colombia', 'Colombia'), ('costa_rica', 'Costa Rica'), ('cuba', 'Cuba'), ('Dominican Republic', 'Dominican Republic'), ('ecuador', 'Ecuador'), ('el_salvador', 'El Salvador'), ('equatorial_guinea', 'Equatorial Guinea'), ('guatemala', 'Guatemala'), ('honduras', 'Honduras'), ('mexico', 'Mexico'), ('nicaragua', 'Nicaragua'), ('panama', 'Panama'), ('paraguay', 'Paraguay'), ('peru', 'Peru'), ('spain', 'Spain'), ('uruguay', 'Uruguay'), ('venezuela', 'Venezuela')], default='all', max_length=32),
        ),
    ]