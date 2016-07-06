import logging

from django.db.models import Q

from properties.models import Property
from properties.serializers import PropertySerializer, CustomPropertyPagination
from properties.utils import get_provinces_from_all_cordinates

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


logger = logging.getLogger(__name__)


class PropertyList(generics.ListCreateAPIView):

    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    pagination_class = CustomPropertyPagination


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Property.objects.all()
    serializer_class = PropertySerializer


@api_view(['GET'])
def get_cordinates(request, ax, ay, bx, by):
    provinces = get_provinces_from_all_cordinates(ax=ax, ay=ay, bx=bx, by=by)

    if not provinces:
        return Response({"foundProperties": 0, "properties": []}, status=404)

    data = set()
    properties = []
    for province in provinces:
        for _property in Property.objects.filter(Q(provinces__contains=province)):
            if _property.id in data:
                continue

            data.add(_property.id)
            properties.append({
                "id": _property.id,
                "title": _property.title,
                "price": _property.price,
                "description": _property.description,
                "x": _property.cordinate_x,
                "y": _property.cordinate_y,
                "beds": _property.bed,
                "baths": _property.bath,
                "squareMeters": _property.squareMeters,
                "provinces": _property.provinces
            })

    if not properties:
        return Response({"foundProperties": 0, "properties": []}, status=404)

    return Response({"foundProperties": len(properties),
                     "properties": properties}, 200)
