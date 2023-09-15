from django.db.models import Count
from rest_framework import generics, permissions, filters
from api.permissions import IsOwnerOrReadOnly
from .models import Resource
from .serializers import ResourceSerializer


class ResourceList(generics.ListCreateAPIView):

    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Resource.objects.annotate(
        favourites_count=Count('favourites', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
        'country_filter',
    ]
    ordering_fields = [
        'favourites_count',
        'favourites__created_at',
        'resource_type_filter',
        'difficulty_level_filter',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ResourceSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Resource.objects.annotate(
        favourites_count=Count('favourites', distinct=True),
    ).order_by('-created_at')
