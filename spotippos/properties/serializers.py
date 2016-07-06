
from rest_framework import serializers, pagination
from rest_framework.response import Response

from properties.models import Property
from properties.utils import get_provinces_from_xy


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = ('id', 'title', 'provinces', 'price', 'description', 'bed', 'bath', 'squareMeters', 'cordinate_x', 'cordinate_y',)

    def create(self, validated_data):

        if validated_data.get('bed') > 5 or validated_data.get('bed') < 1:
            raise serializers.ValidationError({
                'bed': 'The bed must be between 1 and 5.'
            })

        if validated_data.get('bath') > 4 or validated_data.get('bath') < 1:
            raise serializers.ValidationError({
                'bath': 'The bath must be between 1 and 4.'
            })

        if validated_data.get('squareMeters') > 240 or validated_data.get('squareMeters') < 20:
            raise serializers.ValidationError({
                'squareMeters': 'The squareMeters must be between 20 and 240.'
            })

        if validated_data.get('cordinate_x') > 1400 or validated_data.get('cordinate_x') < 0:
            raise serializers.ValidationError({
                'cordinate_x': 'The cordinate_x must be between 0 and 1400.'
            })

        if validated_data.get('cordinate_y') > 1000 or validated_data.get('cordinate_y') < 0:
            raise serializers.ValidationError({
                'cordinate_y': 'The cordinate_y must be between 0 and 1000.'
            })

        provinces = get_provinces_from_xy(x=validated_data['cordinate_x'], y=validated_data['cordinate_y'])

        return Property.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            price=validated_data.get('price'),
            bed=validated_data.get('bed'),
            bath=validated_data.get('bath'),
            provinces=provinces,
            squareMeters=validated_data.get('squareMeters'),
            cordinate_x=validated_data.get('cordinate_x'),
            cordinate_y=validated_data.get('cordinate_y'))


class CustomPropertyPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response(data)
