from django.db import models
from django.contrib.auth.models import User
from resources.models import Resource


class Favourite(models.Model):
    """
    Favourite model, related to 'owner' and 'resource'.
    'owner' is a User instance and 'resource' is a Resource instance.
    'unique_together' makes sure a user can't favourite the same
    resource twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(
        Resource, related_name='favourites', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'resource']

    def __str__(self):
        return f'{self.owner} {self.resource}'
