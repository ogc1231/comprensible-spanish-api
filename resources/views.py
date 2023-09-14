from rest_framework import generics, permissions
from api.permissions import IsOwnerOrReadOnly
from .models import Resource
from .serializers import ResourceSerializer


class ResourceList(generics.ListCreateAPIView):

    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Resource.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ResourceSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Resource.objects.all()
