from rest_framework import serializers

from .models import product


class productSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product
        fields = ('id', 'productname', 'category', 'subcategory',
                  'description', 'images', 'price')
