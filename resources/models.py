from django.db import models
from django.contrib.auth.models import User


class Resource(models.Model):

    country_filter_choices = [
        ('mixed', 'Mixed'),
        ('argentina', 'Argentina'),
        ('bolivia', 'Bolivia'),
        ('canary_islands', 'Canary Islands'),
        ('chile', 'Chile'),
        ('colombia', 'Colombia'),
        ('costa_rica', 'Costa Rica'),
        ('cuba', 'Cuba'),
        ('dominican_republic', 'Dominican Republic'),
        ('ecuador', 'Ecuador'),
        ('el_salvador', 'El Salvador'),
        ('equatorial_guinea', 'Equatorial Guinea'),
        ('guatemala', 'Guatemala'),
        ('honduras', 'Honduras'),
        ('mexico', 'Mexico'),
        ('nicaragua', 'Nicaragua'),
        ('panama', 'Panama'),
        ('paraguay', 'Paraguay'),
        ('peru', 'Peru'),
        ('spain', 'Spain'),
        ('uruguay', 'Uruguay'),
        ('venezuela', 'Venezuela'),
    ]

    resource_type_filter_choices = [
        ('podcast', 'Podcast/Audio'),
        ('youtube', 'YouTube/Video'),
    ]

    difficulty_level_filter_choices = [
        ('learner', 'Learner'),
        ('easy_native', 'Easy Native'),
        ('native', 'Native'),
    ]

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ve6bmd', blank=True
    )
    resource_url = models.URLField(max_length=100, unique=True)
    country_filter = models.CharField(
        max_length=32, choices=country_filter_choices, default='all'
    )
    resource_type_filter = models.CharField(
        max_length=32, choices=resource_type_filter_choices, default='all'
    )
    difficulty_level_filter = models.CharField(
        max_length=32, choices=difficulty_level_filter_choices, default='all'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
