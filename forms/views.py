from rest_framework import generics, permissions, authentication
from api.permissions import IsOwnerOrReadOnly
from .models import ContactForm
from .serializers import ContactFormSerializer


class ContactFormList(generics.ListCreateAPIView):
    '''List all messages or create a new message'''
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    # authentication_classes = [authentication.BasicAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
