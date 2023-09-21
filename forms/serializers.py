from rest_framework import serializers
from forms.models import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = [
            'id', 'name', 'email', 'message', 'created_at',
        ]
