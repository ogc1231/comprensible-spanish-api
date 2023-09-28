from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.permissions import IsOwnerOrReadOnly
from .models import Resource
from .serializers import ResourceSerializer


class ResourceList(generics.ListCreateAPIView):
    """
    List all Resources.
    Create view as Resource if you're the authenicated.
    """
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Resource.objects.annotate(
        favourites_count=Count('favourites', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'favourites__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
        'country_filter',
        'resource_type_filter',
        'difficulty_level_filter',
    ]
    ordering_fields = [
        'favourites_count',
        'favourites__created_at',
        'resource_type_filter',
        'difficulty_level_filter',
        'country_filter',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, edit & delete a Resource if you're the owner.
    """
    serializer_class = ResourceSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Resource.objects.annotate(
        favourites_count=Count('favourites', distinct=True),
    ).order_by('-created_at')
