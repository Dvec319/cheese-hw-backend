from .models import Cheese
from rest_framework import serializers

## Class CheeseSerializer is a subclass of serializers.HyperlinkedModelSerializer.
## For serializing and deserializing data into representations such as json.

class CheeseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model to serialize
        model = Cheese
        # fields to show in json
        fields = ('id', 'name', 'country')


