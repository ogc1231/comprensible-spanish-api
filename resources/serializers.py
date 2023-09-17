from rest_framework import serializers
from resources.models import Resource
from favourites.models import Favourite


class ResourceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    favourite_id = serializers.SerializerMethodField()
    favourites_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_favourite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favourite = Favourite.objects.filter(
                owner=user, resource=obj
            ).first()
            return favourite.id if favourite else None
        return None

    class Meta:
        model = Resource
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'image', 'resource_url',
            'country_filter', 'resource_type_filter',
            'difficulty_level_filter', 'favourite_id',
            'favourites_count', 'desc'
        ]
